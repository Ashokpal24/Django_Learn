from django.db import models
from django.contrib.auth.models import User
from tag.models import Tag


class Article(models.Model):
    title = models.CharField(max_length=200, blank=False)
    content = models.TextField(blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(
        Tag, related_name="articles", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
