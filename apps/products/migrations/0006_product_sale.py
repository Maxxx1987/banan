# Generated by Django 4.0.3 on 2022-04-14 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_property_options_productproperty'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sale',
            field=models.IntegerField(blank=True, default=0, verbose_name='Скидка в процентах'),
        ),
    ]