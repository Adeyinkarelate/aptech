from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    start_date = models.DateField(null=True)
    stop_date = models.DateField(null=True)
    image1 = models.ImageField(upload_to='images',blank=True,null=True)
    image2 = models.ImageField(upload_to='images',blank=True,null=True)
    image3 = models.ImageField(upload_to='images',blank=True,null=True)
    

    def __str__(self):
        return self.title

class SmartPro(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to='images',blank=True,null=True)

    

    def __str__(self):
        return self.title
