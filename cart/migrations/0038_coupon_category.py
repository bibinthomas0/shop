# Generated by Django 4.2.3 on 2023-09-05 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0037_cart_coin_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='category',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
