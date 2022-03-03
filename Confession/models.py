from email import message
from email.policy import default
from django.db import models
import uuid

# Create your models here.
class Confession(models.Model):
    message=models.TextField()
    img=models.ImageField(upload_to="gallery",default="")
    def __str__(self):
        return self.message
    
class Contact(models.Model):
    name=models.CharField(max_length=100)    
    subject=models.CharField(max_length=500)    
    email=models.EmailField(max_length=254)  
    message=models.TextField()  
    
    # def __str__(self):
    #     return self.name+" "+self.subject+" "+self.email+" "+self.message
    
