# Generated by Django 4.1 on 2022-11-02 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_alter_product_inner'),
        ('userapp', '0001_initial'),
        ('ordersapp', '0007_alter_order_cart'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ShopCart',
            new_name='CartItem',
        ),
    ]