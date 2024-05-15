# models.py - Database models for BackEndApi app
from django.db import models

# Define the Person model for storing person data
class Person(models.Model):
    FirstName = models.CharField(max_length=100)  # Field to store the first name (max 100 characters)
    LastName = models.CharField(max_length=100)   # Field to store the last name (max 100 characters)
    Age = models.IntegerField()                   # Field to store the age (integer)