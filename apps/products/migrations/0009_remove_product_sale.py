# Generated by Django 4.0.3 on 2022-04-18 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_remove_event_brand_remove_event_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='sale',
        ),
    ]