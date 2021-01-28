from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    address = models.TextField(max_length=300)

    REQUIRED_FIELDS = ('address', 'first_name', 'last_name')

    def __str__(self):
        return self.username


class Cat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=12)
    breed = models.TextField(max_length=50)
    price = models.IntegerField()
    description = models.TextField(max_length=620, blank=True)
    pic = models.TextField(max_length=300, blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now=True)
    end_date = models.DateTimeField(auto_now=True)
    cats = models.ManyToManyField(Cat, through='CatToOrder')

    def __str__(self):
        return f'{self.id}_{self.user.username}'


class CatToOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def __str__(self):
        return f'Cat_{self.cat.id}_Order_{self.order.id}'








