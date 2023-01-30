import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_url_exists_at_correct_location(client):
    for i in range(1, 7):
        response = client.get(f"/collection/{i}/")
        assert response.status_code == 200
        response = client.get(reverse("pages:collection", args=[f"{i}"]))
        assert response.status_code == 200


@pytest.mark.django_db
def test_correct_template_loaded(client):
    for i in range(1, 7):
        response = client.get(reverse("pages:collection", args=[f"{i}"]))
        assertTemplateUsed(response, '_base.html')
        assertTemplateUsed(response, 'collections/collections_list.html')
        assertTemplateUsed(response, '_menu.html')


@pytest.mark.django_db
def test_correct_content_loaded(client):
    for i in range(1, 7):
        response = client.get(reverse("pages:collection", args=[f"{i}"]))
        content = response.content.decode('utf-8')
        assert "You can choose from any of previously saved collections or download the latest one." in content
        # also checking if database is empty
        assert 'Nothing to display here yet. Click "Fetch new" button.' in content
