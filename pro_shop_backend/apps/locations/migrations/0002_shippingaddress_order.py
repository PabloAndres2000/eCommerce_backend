# Generated by Django 3.2.5 on 2022-08-28 02:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0001_initial'),
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='order',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.order'),
        ),
    ]
