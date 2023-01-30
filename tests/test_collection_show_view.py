import re

import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed
from pages import models
from pages.functions import CATEGORIES


@pytest.mark.django_db
def test_url_exists_at_correct_location(client, fake_csv):
    csvs = models.Collection.objects.all()
    assert len(csvs) == 6
    for i in range(1, 7):
        response = client.get(f"/collection/{i}/?pk={i}")
        assert response.status_code == 200
        response = client.get(reverse("pages:collection", args=[f"{i}"]), {"pk": f"{i}"})
        assert response.status_code == 200


@pytest.mark.django_db
def test_correct_template_loaded(client, fake_csv):
    for i in range(1, 7):
        response = client.get(reverse("pages:collection", args=[f"{i}"]), {"pk": f"{i}"})
        assertTemplateUsed(response, '_base.html')
        assertTemplateUsed(response, 'collections/show_collection.html')
        assertTemplateUsed(response, '_menu.html')


@pytest.mark.django_db
def test_correct_content_loaded(client, fake_csv):
    for i in range(1, 7):
        response = client.get(reverse("pages:collection", args=[f"{i}"]), {"pk": f"{i}"})
        content = response.content.decode('utf-8')
        # are buttons visible
        assert "Show less" in content
        assert "Show more" in content
        # are columns headers visible
        assert "name" in content
        assert "col2" in content
        # is table visible
        assert '<table border="1" class="dataframe">' in content
        # is proper name of the file displayed
        regex = re.compile(f'{CATEGORIES.get(i)}_'+'[0-9]{10}.csv')
        assert len(re.findall(regex, content)) == 1

