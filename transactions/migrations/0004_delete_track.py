# Generated by Django 3.2.8 on 2021-12-10 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_alter_transactions_date_of_birth'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Track',
        ),
    ]
