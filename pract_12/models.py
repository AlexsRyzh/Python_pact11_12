from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=60)
    author = models.CharField(max_length=60)
    price = models.IntegerField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.description


class BookVersion(models.Model):
    version = models.IntegerField()


class Files(models.Model):
    file = models.BinaryField()
    type = models.TextField(blank=True)
