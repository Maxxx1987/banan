import uuid
from django.db import models


class Payment(models.Model):
    STATUSES = (
        ('new', 'Новый'),
        ('pending', 'Обрабатывается'),
        ('error', 'Ошибка'),
        ('success', 'Успешно'),
    )
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    status = models.CharField('Статус', max_length=16, choices=STATUSES, default='new')
    amount = models.IntegerField('Цена', default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
        ordering = ('-id',)


class Purchase(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.PROTECT)
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    payment = models.ForeignKey('payments.Payment', on_delete=models.PROTECT)
    rent_from = models.DateTimeField()
    rent_till = models.DateTimeField()

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ('-id',)


class Order(models.Model):
    STATUSES = (
        ('active', 'Активный'),
        ('complete', 'Завершено'),
        ('void', 'Отменен'),
    )
    identifier = models.UUIDField(default=uuid.uuid4, editable=False)
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, blank=True, null=True)
    session_key = models.CharField(max_length=64, blank=True, null=True)
    payment = models.ForeignKey('payments.Payment', on_delete=models.SET_NULL, blank=True, null=True)
    rent_from = models.DateTimeField(blank=True, null=True)
    rent_till = models.DateTimeField(blank=True, null=True)
    status = models.CharField('Статус', max_length=16, choices=STATUSES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ('-id',)


class ProductOrder(models.Model):
    order = models.ForeignKey('payments.Order', on_delete=models.PROTECT)
    product = models.ForeignKey('products.Product', on_delete=models.PROTECT)
    count = models.PositiveIntegerField('Кол-во', default=1)
