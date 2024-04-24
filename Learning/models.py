from django.db import models


# Create your models here.

class Product(models.Model):
    title = models.CharField(blank=False, max_length=120)    # max_length is required
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(blank=False, decimal_places=2, max_digits=10)
    summary = models.TextField(null=True)
    featured = models.BooleanField(default=True)


class BloodDonor(models.Model):
    BLOOD_GROUPS = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    name = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.name


class BloodRequest(models.Model):
    blood_group = models.CharField(max_length=3)
    quantity = models.PositiveIntegerField()
