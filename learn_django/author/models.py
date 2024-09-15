from django.contrib.auth.models import User
from django.db import models


class AuthorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.user.username

