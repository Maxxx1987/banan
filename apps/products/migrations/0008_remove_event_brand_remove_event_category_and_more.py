# Generated by Django 4.0.3 on 2022-04-18 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='event',
            name='category',
        ),
        migrations.RemoveField(
            model_name='event',
            name='price',
        ),
        migrations.RemoveField(
            model_name='event',
            name='product',
        ),
        migrations.RemoveField(
            model_name='event',
            name='section',
        ),
        migrations.AddField(
            model_name='event',
            name='status',
            field=models.CharField(choices=[('active', 'Активно'), ('complete', 'Завершено'), ('void', 'Отменено')], default='active', max_length=16, verbose_name='Статус'),
        ),
    ]
