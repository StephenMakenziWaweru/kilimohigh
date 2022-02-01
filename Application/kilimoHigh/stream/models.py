from django.db import models
from django.urls import reverse
# Create your models here.
# Create your models here.
class Stream(models.Model):
    STREAM_CHOICES = (("Form 1A", "Form 1A"),
                    ("Form 1B", "Form 1B"),
                    ("Form 1C", "Form 1C"))

    stream_name = models.CharField(max_length=20, choices=STREAM_CHOICES)
    
    def __str__(self):
        return f'{self.stream_name}'

    def get_absolute_url(self):
        return reverse('stream-detail', kwargs={'pk': self.pk})
