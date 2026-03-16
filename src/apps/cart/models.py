from django.db import models

# Create your models here.
class Card(models.Model):
    card_number = models.CharField(max_length=16)
    phone = models.CharField(max_length=13)
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20)
    expire = models.DateField()

    def __str__(self):
        return self.card_number
