from django.db import models


# Create your models here.

class Product(models.Model):
    title = models.CharField(blank=False, max_length=120)    # max_length is required
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(blank=False, decimal_places=2, max_digits=10)
    summary = models.TextField(null=True)
    featured = models.BooleanField(default=True)

