from django.contrib import admin

from apps.products.models import Product, Brand, Property, ProductProperty


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    pass

@admin.register(ProductProperty)
class ProductPropertyAdmin(admin.ModelAdmin):
    pass
