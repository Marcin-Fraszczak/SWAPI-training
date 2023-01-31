import re

import pytest
from django.urls import reverse
from pages.models import Collection
from pages.functions import CATEGORIES


@pytest.mark.full
@pytest.mark.django_db
def test_full_program_people(client):
    i = 1
    objects_before = Collection.objects.all().count()
    response = client.get(reverse("pages:collection", args=[f"{i}"]),
                          {"fetch": 1})
    objects_after = Collection.objects.all().count()
    last_object = Collection.objects.all().last()
    assert response.status_code == 302
    assert response.url == reverse("pages:collection", args=[f"{i}"])
    assert objects_after - objects_before == 1
    regex = re.compile(f'{CATEGORIES.get(i)}_' + '[0-9]{10}.csv')
    assert len(re.findall(regex, last_object.filename)) == 1


@pytest.mark.django_db
def test_full_program_planets(client):
    i = 2
    objects_before = Collection.objects.all().count()
    response = client.get(reverse("pages:collection", args=[f"{i}"]),
                          {"fetch": 1})
    objects_after = Collection.objects.all().count()
    last_object = Collection.objects.all().last()
    assert response.status_code == 302
    assert response.url == reverse("pages:collection", args=[f"{i}"])
    assert objects_after - objects_before == 1
    regex = re.compile(f'{CATEGORIES.get(i)}_' + '[0-9]{10}.csv')
    assert len(re.findall(regex, last_object.filename)) == 1


@pytest.mark.django_db
def test_full_program_films(client):
    i = 3
    objects_before = Collection.objects.all().count()
    response = client.get(reverse("pages:collection", args=[f"{i}"]),
                          {"fetch": 1})
    objects_after = Collection.objects.all().count()
    last_object = Collection.objects.all().last()
    assert response.status_code == 302
    assert response.url == reverse("pages:collection", args=[f"{i}"])
    assert objects_after - objects_before == 1
    regex = re.compile(f'{CATEGORIES.get(i)}_' + '[0-9]{10}.csv')
    assert len(re.findall(regex, last_object.filename)) == 1


@pytest.mark.django_db
def test_full_program_species(client):
    i = 4
    objects_before = Collection.objects.all().count()
    response = client.get(reverse("pages:collection", args=[f"{i}"]),
                          {"fetch": 1})
    objects_after = Collection.objects.all().count()
    last_object = Collection.objects.all().last()
    assert response.status_code == 302
    assert response.url == reverse("pages:collection", args=[f"{i}"])
    assert objects_after - objects_before == 1
    regex = re.compile(f'{CATEGORIES.get(i)}_' + '[0-9]{10}.csv')
    assert len(re.findall(regex, last_object.filename)) == 1


@pytest.mark.django_db
def test_full_program_vehicles(client):
    i = 5
    objects_before = Collection.objects.all().count()
    response = client.get(reverse("pages:collection", args=[f"{i}"]),
                          {"fetch": 1})
    objects_after = Collection.objects.all().count()
    last_object = Collection.objects.all().last()
    assert response.status_code == 302
    assert response.url == reverse("pages:collection", args=[f"{i}"])
    assert objects_after - objects_before == 1
    regex = re.compile(f'{CATEGORIES.get(i)}_' + '[0-9]{10}.csv')
    assert len(re.findall(regex, last_object.filename)) == 1


@pytest.mark.django_db
def test_full_program_starships(client):
    i = 6
    objects_before = Collection.objects.all().count()
    response = client.get(reverse("pages:collection", args=[f"{i}"]),
                          {"fetch": 1})
    objects_after = Collection.objects.all().count()
    last_object = Collection.objects.all().last()
    assert response.status_code == 302
    assert response.url == reverse("pages:collection", args=[f"{i}"])
    assert objects_after - objects_before == 1
    regex = re.compile(f'{CATEGORIES.get(i)}_' + '[0-9]{10}.csv')
    assert len(re.findall(regex, last_object.filename)) == 1
