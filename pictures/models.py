from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length =50)

    def __str__(self):
        return self.name      

    def save_location(self):
      self.save()  


    def delete_location(self):
      self.save()   
    

class Category(models.Model):
    name = models.CharField(max_length =50)

    def __str__(self):
        return self.name 

    def save_category(self):
      self.save()  

    def delete_category(self):
      self.save()           

class Image(models.Model):
    image = models.ImageField()
    image_name =models.CharField(max_length=50)
    image_description = models.TextField() 
    location = models.ForeignKey(Location, on_delete=models.CASCADE) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
      return self.first_name 

    def save_image(self):
      self.save()  


    def delete_image(self):
      self.save()   


