from django.db import models

# Model containing the data which we want to store and use
class Person(models.Model):
    FirstName = models.CharField(max_length=100) # First name of person with a max character length of 100 characters
    LastName = models.CharField(max_length=100) # Last name of person with a max character length of 100 characters
    Age = models.IntegerField() # Age of person of type integer