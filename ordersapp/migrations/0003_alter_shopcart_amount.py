# Generated by Django 4.1 on 2022-10-26 10:46

from django.db import migrations, models
import ordersapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('ordersapp', '0002_shopcart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopcart',
            name='amount',
            field=models.PositiveSmallIntegerField(default=1, validators=[ordersapp.models.validate_amount]),
        ),
    ]
