from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    email = models.TextField()
    mailing_address = models.TextField()
    name = models.TextField(max_length=20)
    phone = models.TextField(max_length=14)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    order_date = models.DateField()


class Product(models.Model):
    description = models.TextField()
    name = models.CharField(max_length=20)
    price = models.FloatField()
    product_id = models.CharField(max_length=5)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField()
