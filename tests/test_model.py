import pytest
from pages import models


@pytest.mark.django_db
def test_instance_properly_created(fake_df):
    objects_before = models.Collection.objects.all().count()
    models.Collection.objects.create(category=1, filename="test.csv")
    object = models.Collection.objects.get(filename="test.csv")
    objects_after = models.Collection.objects.all().count()
    assert object
    assert objects_after - objects_before == 1
    # check __str__ method
    assert str(object) == "test.csv"


