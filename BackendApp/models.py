from django.db import models

class Docter(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  profession = models.CharField(max_length=255)
  salary = models.IntegerField()