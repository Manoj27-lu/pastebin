from django.urls import path
from .views import healthz, create_paste, fetch_paste, view_paste

urlpatterns = [
    path('api/healthz', healthz),
    path('api/pastes', create_paste),
    path('api/pastes/<uuid:id>', fetch_paste),
    path('p/<uuid:id>', view_paste),
]
