from django.db import models
from django.db.models.enums import Choices

# Create your models here.


class Add_member(models.Model):
    group = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    )
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    phone_number = models.IntegerField()
    blood_group = models.CharField(max_length=4, choices=group)