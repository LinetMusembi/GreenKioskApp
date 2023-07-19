from django.db import models

class Delivery(models.Model):
    customer_name = models.CharField(max_length=40)
    delivery_address = models.CharField(max_length=70)
    total_cost = models.DecimalField(max_digits=8,decimal_places=2)
    delivery_date = models.DateField()
    status = models.CharField(max_length=50)

