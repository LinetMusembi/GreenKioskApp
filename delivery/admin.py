from django.contrib import admin

from .models import Delivery
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ("customer_name","delivery_address","total_cost","delivery_date","status")    


admin.site.register(Delivery,DeliveryAdmin)    