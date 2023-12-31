from django.db import models

# Create your models here.
class Order(models.Model):
   order_id = models.AutoField(primary_key=True)
   name = models.CharField(max_length=50)
   order_items = models.TextField()
   total_cost = models.DecimalField(max_digits=8,decimal_places=2)
   delivery_address = models.CharField(max_length=100)
   delivery_date = models.DateField()
   status = models.CharField(max_length=50)
