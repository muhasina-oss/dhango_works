from django.db import models

# Create your models here.
class Books(models.Model):
  
  title = models.CharField(max_length=200)
  
  author= models.CharField(max_length=200)
  
  price = models.PositiveIntegerField()
  
  pages = models.PositiveIntegerField()
  
  publications = models.CharField(max_length=200)