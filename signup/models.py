from django.db import models

# Create your models here.
class Signup(models.Model):
    client_name = models.CharField(max_length=30)
    email = models.EmailField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=10)
    date_birth = models.DateField()
   

