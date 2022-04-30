from django.contrib import admin

from apps.payments.models import Order, ProductOrder


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductOrder)
class ProductOrderAdmin(admin.ModelAdmin):
    pass
