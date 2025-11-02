"""Root URL configuration for the SelfLink project."""

from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


def healthcheck(_request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("admin/", admin.site.urls),
    path("health/", healthcheck, name="healthcheck"),
    path("api/v1/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("api/v1/users/", include("apps.users.urls")),
]
