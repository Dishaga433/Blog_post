from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_seller=models.BooleanField(default=False)
    is_customer=models.BooleanField(default=False)


class Seller(models.Model):

    user=models.OneToOneField(Login,on_delete=models.CASCADE,related_name="Seller")
    name=models.CharField(max_length=20)
    ph_no=models.CharField(max_length=10)
    email=models.EmailField()


class Customer(models.Model):

    user=models.OneToOneField(Login,on_delete=models.CASCADE,related_name="Customer")
    name=models.CharField(max_length=20)
    ph_no=models.CharField(max_length=10)
    email=models.EmailField()



class Blog(models.Model):
    seller_name = models.ForeignKey('Seller', on_delete=models.CASCADE)
    title =models.CharField(max_length=20)
    content=models.TextField()
    author_name=models.CharField(max_length=20)
    date=models.DateField()
    document = models.FileField(upload_to='documents/')


