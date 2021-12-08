# Generated by Django 3.2.8 on 2021-12-07 23:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_customers_created_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='created_datetime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
