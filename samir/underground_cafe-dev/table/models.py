from django.db import models
from django import forms

# Create your models here.
class Table(models.Model):
	name=models.CharField(max_length=125)
	zone=models.CharField(max_length=125)
	is_active=models.BooleanField()