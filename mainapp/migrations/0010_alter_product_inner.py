# Generated by Django 4.1 on 2022-10-24 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_alter_image_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='inner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='mainapp.inner'),
        ),
    ]