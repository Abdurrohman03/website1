from django.db import models


class Blogs(models.Model):
    title = models.CharField(max_length=32)
    content = models.TextField()
