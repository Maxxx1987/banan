# Generated by Django 4.0.3 on 2022-04-11 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_brand'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'verbose_name': 'Брэнд', 'verbose_name_plural': 'Брэнды'},
        ),
        migrations.AddField(
            model_name='brand',
            name='icon',
            field=models.ImageField(blank=True, upload_to='mediafiles/icons/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.brand'),
        ),
    ]
