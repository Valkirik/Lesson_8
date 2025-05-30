from django.db import models
from django.contrib.auth.models import User



class DataTimeMixin:
    data_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)



class Page(models.Model, DataTimeMixin):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_privet = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.pk} - {self.title}"


    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"
