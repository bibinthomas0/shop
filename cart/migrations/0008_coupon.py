# Generated by Django 4.2.2 on 2023-08-06 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_alter_order_total_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True)),
                ('discount', models.FloatField()),
                ('valid_from', models.DateTimeField()),
                ('valid_to', models.DateTimeField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
