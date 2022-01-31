from email import message
from django.db import models

# Create your models here.
class Confession(models.Model):
    message=models.TextField()
    def __str__(self):
        return self.message
    
class Contact(models.Model):
    name=models.CharField(max_length=100)    
    subject=models.CharField(max_length=500)    
    email=models.EmailField(max_length=254)  
    message=models.TextField()  
    
    # def __str__(self):
    #     return self.name+" "+self.subject+" "+self.email+" "+self.message
    
