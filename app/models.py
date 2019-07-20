from django.db import models
from django.urls import reverse 

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=0)
    adress = models.CharField(max_length=200)
    images = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self): 
        return reverse('field_detail', args=[str(self.id)])

class User(models.Model):
    user = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.user
