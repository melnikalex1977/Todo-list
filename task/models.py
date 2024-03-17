from django.db import models
from datetime import datetime
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)


    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=255)
    datetime = models.TextField(max_length=255, default="")
    deadline = models.TextField(max_length=255, default="")
    published_date = models.DateTimeField(default=timezone.now)
    task_is_done = models.BooleanField(default=False)
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def get_tag_name(self):
        return self.tags.name

    class Meta:
        ordering = ("content", )

    def __str__(self):
        return self.content
