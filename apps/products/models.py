from autoslug import AutoSlugField
from django.db import models


class Brand(models.Model):
    title = models.CharField('Название', max_length=255)
    description = models.TextField('Описание')
    icon = models.ImageField(upload_to='mediafiles/icons/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Брэнд'
        verbose_name_plural = 'Брэнды'


class Product(models.Model):
    title = models.CharField('Название', max_length=255)
    slug = AutoSlugField(populate_from='title')
    description = models.TextField('Описание')
    image = models.ImageField(upload_to='mediafiles/covers/%Y/%m/%d', blank=True)
    section = models.ForeignKey('catalog.Section', on_delete=models.CASCADE, related_name='products')
    price = models.PositiveIntegerField('Цена', default=0)
    brand = models.ForeignKey('products.Brand', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def get_absolut_url(self):
        return f'/products/{self.id}/'


class Property(models.Model):
    title = models.CharField('Название', max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Спецификация'
        verbose_name_plural = 'Спецификации'


class ProductProperty(models.Model):
    product = models.ForeignKey('products.Product',on_delete=models.CASCADE)
    property = models.ForeignKey('products.Property',on_delete=models.CASCADE)
    value = models.CharField('Значение', max_length=255)
