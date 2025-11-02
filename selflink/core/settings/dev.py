"""Development settings for the SelfLink Django project."""

from .base import *  # noqa: F401,F403


DEBUG = True
ALLOWED_HOSTS = [
    *ALLOWED_HOSTS,  # type: ignore[name-defined]
    "localhost",
    "127.0.0.1",
]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Enable browsable API authentication in development.
REST_FRAMEWORK["DEFAULT_AUTHENTICATION_CLASSES"] = [  # type: ignore[name-defined]
    "rest_framework.authentication.SessionAuthentication",
    "rest_framework.authentication.BasicAuthentication",
]

# Allow hosts for local dev tools such as ngrok if configured via env.
EXTRA_ALLOWED_HOSTS = env.list("DJANGO_DEV_EXTRA_ALLOWED_HOSTS", default=[])  # type: ignore[name-defined]
ALLOWED_HOSTS.extend(EXTRA_ALLOWED_HOSTS)  # type: ignore[attr-defined]
