from django.db import models


class Order(models.Model):
    product = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()