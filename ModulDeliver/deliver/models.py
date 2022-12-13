from django.db import models


# Create your models here.


class Order(models.Model):
    name = models.CharField(max_length=255, primary_key=True)


    def __str__(self):
        return f'{self.name}'


class Box(models.Model):
    name = models.CharField(max_length=255)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='boxes')

    def __str__(self):
        return f'{self.order.name}: {self.name}'


class Good(models.Model):
    name = models.CharField(max_length=255)
    box = models.ManyToManyField(Box, related_name='goods')

    def __str__(self):
        return f'{self.name}'
