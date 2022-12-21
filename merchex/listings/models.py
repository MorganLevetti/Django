from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Band(models.Model):
    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(max_length=50)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2022)]
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.fields.CharField(max_length=100)
    type = models.fields.CharField(max_length=100)
    price = models.fields.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(9000)]
    )
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)
