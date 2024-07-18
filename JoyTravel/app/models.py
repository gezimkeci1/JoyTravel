from django.db import models
from django.utils.text import slugify

class City(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.country}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}, {self.country}"

class Hotel(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='hotels', blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='hotel_images/', blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    price_per_night_adult = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    price_per_night_child = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    contactName = models.CharField(max_length=50, blank=True, null=True)
    contactLastName = models.CharField(max_length=50, blank=True, null=True)
    contactEmail = models.EmailField(blank=True, null=True)
    contactMessage = models.TextField(max_length=1500, blank=True, null=True)

    def __str__(self):
        return f"{self.contactName} {self.contactLastName}"
    
class Flight(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='flights', blank=True, null=True)
    image = models.ImageField(upload_to='flight_images/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.city}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} {self.city}"