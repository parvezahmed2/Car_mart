from django.db import models
from brand.models import CarModel
from django.contrib.auth.models import User
# Create your models here.

class Car(models.Model):
    model_name = models.CharField(max_length = 50)
    description = models.TextField()
    price = models.IntegerField()
    quantity = models.PositiveIntegerField(default=0)
    brand = models.ForeignKey(CarModel, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='uploads', blank=True, null = True)

    def __str__(self):
        return self.model_name



class Comment(models.Model):
    post = models.ForeignKey(Car, on_delete = models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Comments by {self.name}"
