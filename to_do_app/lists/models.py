from django.db import models
# from django.utils import timezone               it will not show exact current time
from datetime import datetime

class List(models.Model):
    title = models.CharField(max_length=100)
    details = models.CharField()
    date = models.DateTimeField(default=datetime.now)
    complete=models.BooleanField(default=False)

    def __str__(self):
        return self.title