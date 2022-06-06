import datetime
from django.db import models
from django.utils import timezone

class Person(models.Model):
    identification_no = models.TextField(primary_key=True, max_length=50)
    first_name = models.TextField(max_length=25)
    last_name = models.TextField(max_length=25)
    dob = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
