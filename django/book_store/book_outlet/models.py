from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
# Create your models here.


class Book(models.Model):
    # id = models.AutoField() added automaticaly
    title = models.CharField(max_length=100)
    author = models.CharField(null=True, max_length=100)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    is_bestselling = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} ({self.rating})"

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.id])
