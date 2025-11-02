from django.urls import reverse

from rest_framework.test import APIClient


def test_ping_returns_ok():
    client = APIClient()
    response = client.get(reverse("users:ping"))

    assert response.status_code == 200
    assert response.json() == {"status": "users-ok"}

