from django.contrib import admin

from .models import Store
class StoreAdmin(admin.ModelAdmin):
    list_display =("product_id","product_name","price","quantity","category","store_name","store_name")
admin.site.register(Store,StoreAdmin)  

