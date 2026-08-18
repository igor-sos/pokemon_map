from django.db import models  # noqa F401


class Post(models.Model):
    title = models.CharField(max_length=200)