from django.contrib.auth.forms import UserCreationForm
from . import models


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = models.CustomUser
