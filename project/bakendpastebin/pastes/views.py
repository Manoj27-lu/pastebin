import json
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.http import JsonResponse, Http404
from django.shortcuts import get_object_or_404, render
from django.conf import settings
from .models import Paste


def get_now(request):
    """Helper function for deterministic time handling in tests.
    
    If TEST_MODE is enabled and x-test-now-ms header is present,
    use that as the current time. Otherwise use system time.
    """
    if settings.TEST_MODE and request.headers.get("x-test-now-ms"):
        return timezone.datetime.fromtimestamp(
            int(request.headers["x-test-now-ms"]) / 1000,
            tz=timezone.utc
        )
    return timezone.now()


def healthz(request):
    """Health check endpoint."""
    try:
        from django.db import connection
        connection.ensure_connection()
        return JsonResponse({"ok": True})
    except Exception:
        return JsonResponse({"ok": False}, status=500)


@csrf_exempt
def create_paste(request):
    """Create a new paste."""
    if request.method != 'POST':
        return JsonResponse({"error": "Method not allowed"}, status=405)

    try:
        data = json.loads(request.body)
        content = data.get("content")
        ttl = data.get("ttl_seconds")
        max_views = data.get("max_views")

        if not content or not isinstance(content, str):
            return JsonResponse({"error": "Invalid content"}, status=400)

        expires_at = None
        if ttl:
            expires_at = timezone.now() + timezone.timedelta(seconds=int(ttl))

        paste = Paste.objects.create(
            content=content,
            expires_at=expires_at,
            max_views=max_views
        )

        return JsonResponse({
            "id": str(paste.id),
            "url": f"{request.scheme}://{request.get_host()}/p/{paste.id}"
        }, status=201)

    except Exception:
        return JsonResponse({"error": "Invalid request"}, status=400)


def fetch_paste(request, id):
    """Fetch paste as JSON (counts views)."""
    paste = get_object_or_404(Paste, id=id)
    now = get_now(request)

    if paste.is_expired(now):
        return JsonResponse({"error": "Not found"}, status=404)

    paste.views += 1
    paste.save()

    remaining_views = None
    if paste.max_views is not None:
        remaining_views = max(paste.max_views - paste.views, 0)

    return JsonResponse({
        "content": paste.content,
        "remaining_views": remaining_views,
        "expires_at": paste.expires_at
    })


def view_paste(request, id):
    """View paste as HTML (counts views)."""
    paste = get_object_or_404(Paste, id=id)
    now = get_now(request)

    if paste.is_expired(now):
        raise Http404()

    paste.views += 1
    paste.save()

    return render(request, "paste.html", {"content": paste.content})
