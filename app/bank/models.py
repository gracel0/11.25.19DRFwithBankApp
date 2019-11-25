from django.db import models

# Create your models here.

class Branch (models.Model):
    bank_name = models.CharField(max_length=50)
    def __str__ (self):
        return self.bank_name
    class Meta:
        verbose_name_plural= 'branches'

class Customer (models.Model):
    customer_name = models.CharField(max_length=50)
    def __str__ (self):
        return.self.customer_name



