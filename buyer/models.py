from django.db import models

# Create your models here.


class Buyer(models.Model):
   customer_id = models.AutoField(primary_key=True)
   name = models.CharField(max_length=50)
   phone = models.CharField(max_length=50)
   email = models.EmailField()
#    orders = models.ManyToManyField()
   loyalty_points = models.IntegerField()

