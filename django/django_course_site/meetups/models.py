from django.db import models

# Create your models here.


class Meetups(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=800)
    # location = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Meetups'
        verbose_name_plural = 'Meetups'

    def __str__(self):
        return self.title
