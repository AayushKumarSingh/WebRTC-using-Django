from django import forms
from .models import BloodDonor, BloodRequest

BLOOD_GROUPS = (
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
)


class BloodDonationForm(forms.ModelForm):
    class Meta:
        model = BloodDonor
        fields = ['name', 'blood_group', 'email', 'phone', 'address']


class BloodRequestForm(forms.ModelForm):
    class Meta:
        model = BloodRequest
        fields = ['blood_group', 'quantity']