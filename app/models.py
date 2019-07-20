from django.db import models
from django.urls import reverse 

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=0)
    adress = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self): 
        return reverse('field_detail', args=[str(self.id)])