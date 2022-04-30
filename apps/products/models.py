import datetime
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
    _price = models.PositiveIntegerField('Цена', default=0, db_column='price')
    brand = models.ForeignKey('products.Brand', on_delete=models.SET_NULL, blank=True, null=True)

    @property
    def base_price(self):
        return self._price

    @property
    def price(self):
        now = datetime.datetime.now()
        price = self._price
        sale = None

        active_events = Event.objects.filter(actual_from__lt=now, actual_till__gt=now)
        for event in active_events:
            category_event = event.categoryevent_set.first()
            if category_event:
                if category_event.category_id == self.section.category_id:
                    sale = event.sale
                    break
            else:
                sale = event.sale

        if sale:
            price = int(self._price * (100 - sale) / 100)

        return price

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def get_absolute_url(self):
        return f'/products/{self.pk}/'


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

    class Meta:
        verbose_name = 'Характеристики товара'
        verbose_name_plural = 'Характеристики товара'


class Event(models.Model):
    title = models.CharField('Название', max_length=255)
    slug = AutoSlugField(populate_from='title')
    description = models.TextField('Описание')
    sale = models.IntegerField('Скидка в процентах', blank=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    actual_from = models.DateTimeField()
    actual_till = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'

    def get_absolut_url(self):
        return f'/events/{self.id}/'


class CategoryEvent(models.Model):
    category = models.ForeignKey('catalog.Category', on_delete=models.CASCADE)
    event = models.ForeignKey('products.Event', on_delete=models.CASCADE)

    def __str__(self):
        return self.event

    class Meta:
        verbose_name = 'Акция на группу товаров'
        verbose_name_plural = 'Акция на группу товаров'


class Store(models.Model):
    title = models.CharField('Название', max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'


class ProductStore(models.Model):
    product = models.ForeignKey('products.Product',on_delete=models.CASCADE)
    store = models.ForeignKey('products.Store',on_delete=models.CASCADE)
    amount = models.IntegerField('Количество', default=0)

    class Meta:
        verbose_name = 'Наличие товара'
        verbose_name_plural = 'Наличие товара'

    def is_stock(self):
        return self.amount > 0

