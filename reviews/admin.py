from django.contrib import admin

# Register your models here.
from .models import Reviews

class ReviewsAdmin(admin.ModelAdmin):
    list_display = ("product_id","review_text","rating","reviewer_name","date_added","num_votes")

admin.site.register(Reviews,ReviewsAdmin)    

