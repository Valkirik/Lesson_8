from django.db import models
from book.models import Book

class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    book = models.ManyToManyField(Book)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"