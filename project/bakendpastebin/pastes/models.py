import uuid
from django.db import models
from django.utils import timezone


class Paste(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    max_views = models.IntegerField(null=True, blank=True)
    views = models.IntegerField(default=0)

    def is_expired(self, now):
        if self.expires_at and now >= self.expires_at:
            return True
        if self.max_views is not None and self.views >= self.max_views:
            return True
        return False

    def __str__(self):
        return f"Paste {self.id}"
