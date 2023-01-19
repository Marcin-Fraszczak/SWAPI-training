from django.contrib.auth import get_user_model
from django.db import models

CATEGORIES = (
    (1, "people"),
    (2, "planets"),
    (3, "films"),
    (4, "species"),
    (5, "vehicles"),
    (6, "starships"),
)
User = get_user_model()


class Collection(models.Model):
    category = models.IntegerField(choices=CATEGORIES)
    filename = models.CharField(max_length=64)
    created = models.DateTimeField(auto_now=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.filename
