from django.contrib import admin

# Register your models here.
from .models import Order

@admin.register(Order)
class  OrderAdmin(admin.ModelAdmin):
    list_display = ['product_category', 'payment_method', 'shipping_cost', 'unit_price']
