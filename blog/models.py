from django.db import models
from django.utils import timezone


class AuthorTable(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    address = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class BlogTable(models.Model):
    author = models.ForeignKey(AuthorTable, on_delete=models.CASCADE)
    blog = models.TextField(max_length=500)
    created_at = models.DateField(default=timezone.now)
    updated_at = models.DateField(blank=True)

    def __str__(self):
        return str(self.id)
