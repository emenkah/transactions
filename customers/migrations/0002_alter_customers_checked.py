# Generated by Django 3.2.8 on 2021-12-06 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='checked',
            field=models.BooleanField(blank=True, null=True, verbose_name='Checked'),
        ),
    ]
