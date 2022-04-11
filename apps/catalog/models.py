from django.db import models
from autoslug import AutoSlugField


class Category(models.Model):
    title = models.CharField(max_length=155)
    slug = AutoSlugField(populate_from='title')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('order',)

    def get_absolut_url(self):
        return f'/catalog/{self.slug}/'


class Section(models.Model):
    category = models.ForeignKey('catalog.Category', on_delete=models.CASCADE)
    title = models.CharField(max_length=155)
    slug = AutoSlugField(populate_from='title')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title} ({self.category.title})'

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
        ordering = ('order',)

    def get_absolut_url(self):
        return f'/catalog/{self.category.slug}/{self.slug}/'


