# Generated by Django 4.1.1 on 2022-10-22 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_mainsection'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='mainsection',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.mainsection'),
        ),
    ]
