from django.db import models

class Table(models.Model):
    name=models.CharField(max_length=255)
    outlet_zone=models.CharField(max_length=255)
    is_active=models.BooleanField()

    def __str__(self):
        return self.name
