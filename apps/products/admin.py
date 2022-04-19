from django.contrib import admin

from apps.products.models import Product, Brand, Property, ProductProperty, Event, CategoryEvent
from apps.products.forms import EventAdminForm


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', '_price')


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductProperty)
class ProductPropertyAdmin(admin.ModelAdmin):
    pass


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'sale', 'created_at', 'actual_from', 'actual_till')
    list_editable = ('sale', 'actual_from', 'actual_till')
    form = EventAdminForm


@admin.register(CategoryEvent)
class CategoryEventAdmin(admin.ModelAdmin):
    pass


