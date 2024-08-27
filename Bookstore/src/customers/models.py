from django.db import models

# Create your models here.
class Customer(models.Model):
    name= models.CharField(max_length=120)
    notes= models.TextField()
    pic = models.ImageField(upload_to='customers', default='default.jpg') 
    
    def __str__(self):
        return str(self.name)   