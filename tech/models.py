from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    start_date = models.DateField(null=True)
    stop_date = models.DateField(null=True)
    image1 = CloudinaryField('event1')
    image2 = CloudinaryField('event2')
    image3 = CloudinaryField('event3')
    

    def __str__(self):
        return self.title

class SmartPro(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = CloudinaryField('smartpro')

    

    def __str__(self):
        return self.title
