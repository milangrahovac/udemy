from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Countries"


class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=6)
    city = models.CharField(max_length=50)
    # country = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.street}, {self.postal_code}, {self.city}"

    class Meta:
        verbose_name_plural = "Address Entries"


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(
        Address, on_delete=models.CASCADE, null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Book(models.Model):
    # id = models.AutoField() - added automaticaly
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, related_name="books")
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True,
                            null=False, db_index=True)  # editable=False slug: Harry Potter 1 -> harry-potter-1
    published_countries = models.ManyToManyField(Country, null=False)

    def __str__(self):
        return f"{self.title} ({self.rating})"

    def get_absolute_url(self):
        # return reverse("book-detail", args=[self.id])
        return reverse("book-detail", args=[self.slug])

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)
