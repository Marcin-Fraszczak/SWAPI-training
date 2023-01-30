import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


def test_url_exists_at_correct_location(client):
    response = client.get("/")
    assert response.status_code == 200
    response = client.get(reverse("pages:home"))
    assert response.status_code == 200


def test_correct_template_loaded(client):
    response = client.get(reverse("pages:home"))
    assertTemplateUsed(response, '_base.html')
    assertTemplateUsed(response, 'collections/homepage.html')
    assertTemplateUsed(response, '_menu.html')


def test_correct_content_loaded(client):
    response = client.get(reverse("pages:home"))
    content = response.content.decode('utf-8')
    assert "Welcome to the STAR WARS Explorer app." in content
