from django.db import models
from datetime import datetime, timedelta
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)


    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=255)
    datetime = models.DateTimeField(default=timezone.now)
    deadline = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)
    task_is_done = models.BooleanField(default=False)
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.datetime:
            self.datetime = timezone.now()
        self.deadline = self.deadline or timezone.now() + timedelta(days=1)
        self.published_date = self.published_date or timezone.now() + timedelta(days=2)
        super(Task, self).save(*args, **kwargs)
    def get_tag_name(self):
        return self.tags.name

    class Meta:
        ordering = ("content", )

    def __str__(self):
        return self.content
