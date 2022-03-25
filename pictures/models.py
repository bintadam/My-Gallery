from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField()
    image_name =models.CharField(max_length=70)
    image_description = models.TextField() 
    location = models.ForeignKey() 

    def __str__(self):
      return self.first_name 

    def save_image(self):
      self.save()  


    def delete_image(self):
      self.save()   


class Location(models.Model):
    name = models.CharField(max_length =50)

    def __str__(self):
        return self.name      

    def save_location(self):
      self.save()  


    def delete_location(self):
      self.save()   
    