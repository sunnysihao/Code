# Generated by Django 4.0.3 on 2022-04-07 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_ordermedicine_order_medicines_ordermedicine_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='medicines',
        ),
    ]
