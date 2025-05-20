from django.db import models

class Author(models.Model):
    full_name = models.CharField(max_length=200)


class Book(models.Model):
    title = models.CharField(max_length=100, default="title")
    price = models.FloatField(default="0.00")
    genre = models.CharField(max_length=100, default="genre")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.title} - {self.genre}"


