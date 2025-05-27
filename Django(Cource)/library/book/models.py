from django.db import models

class Author(models.Model):
    full_name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.full_name}"


class Language(models.Model):
    lang = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.lang}"

class Book(models.Model):
    title = models.CharField(max_length=100, default="title")
    price = models.FloatField(default="0.00")
    genre = models.CharField(max_length=100, default="genre")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.SET_DEFAULT, default=None, null=True)

    def __str__(self):
        return f"{self.title} - {self.author}"


