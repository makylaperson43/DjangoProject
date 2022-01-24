from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=200, null=True)
    author = models.CharField(max_length=200, null=True)
    genre = models.CharField(max_length=200, null=True, blank=True)
    summary = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name 



