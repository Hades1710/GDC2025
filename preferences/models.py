from django.db import models
from donor.models import Donor

# Create your models here.

class StudentBackground(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    donors = models.ManyToManyField(Donor, related_name='student_backgrounds')

    def __str__(self):
        return self.name

class EducationalInterest(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    donors = models.ManyToManyField(Donor, related_name='educational_interests')

    def __str__(self):
        return self.name

class SpecificNeed(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    donors = models.ManyToManyField(Donor, related_name='specific_needs')

    def __str__(self):
        return self.name
