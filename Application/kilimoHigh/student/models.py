from datetime import date
from django.db import models
from django.urls import reverse
from stream.models import Stream

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_admission = models.DateField(default=date.today)
    guardian = models.CharField(max_length=100)
    stream_name = models.ForeignKey(Stream, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('detailedstudent', kwargs={'pk': self.pk})
