from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField()
    image_name =models.CharField(max_length=70)
    image_description = models.TextField()  

    def __str__(self):
      return self.first_name  


class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name      