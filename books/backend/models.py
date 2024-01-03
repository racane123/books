from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=255)
    genre = models.ManyToManyField('Genre')
    summary = models.TextField()
    published_date = models.DateField()

    def __str__(self):
        return self.title


class Genre(models.Model):
    genre_name = models.CharField(max_length=255)

    def __str__(self):
        return self.genre_name
