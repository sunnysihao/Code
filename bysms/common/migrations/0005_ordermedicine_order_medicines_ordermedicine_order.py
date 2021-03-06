# Generated by Django 4.0.3 on 2022-04-07 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_medicine_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderMedicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.medicine')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='medicines',
            field=models.ManyToManyField(through='common.OrderMedicine', to='common.medicine'),
        ),
        migrations.AddField(
            model_name='ordermedicine',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.order'),
        ),
    ]
