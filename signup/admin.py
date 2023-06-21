from django.contrib import admin

# Register your models here.
from .models import Signup
class SignupAdmin(admin.ModelAdmin):
    list_display = ("client_name","email","first_name","last_name","phone_number","date_birth")
admin.site.register(Signup,SignupAdmin)    



    
     
