from django.db import models
# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)

    class Meta:
        verbose_name_plural = "Locations"

    def __str__(self):
        return f"{self.name} ({self.address})"


class Participant(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name_plural = "Participants"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()

    # Sets the column name in the admin display
    full_name.short_description = 'Full Name'


class Meetup(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=800)
    image = models.ImageField(upload_to="images")
    # location - one to many relatition
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    # participant - many to many relatition
    participant = models.ManyToManyField(Participant, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Meetups"

    def __str__(self):
        return self.title
