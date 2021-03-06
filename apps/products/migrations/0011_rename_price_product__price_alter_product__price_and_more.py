# Generated by Django 4.0.3 on 2022-04-19 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_section'),
        ('products', '0010_remove_event_status_event_is_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='_price',
        ),
        migrations.AlterField(
            model_name='product',
            name='_price',
            field=models.PositiveIntegerField(db_column='price', default=0, verbose_name='Цена'),
        ),
        migrations.CreateModel(
            name='CategoryEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.event')),
            ],
        ),
    ]
