# Generated by Django 4.1.1 on 2022-10-22 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_section_mainsection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inner',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inners', to='mainapp.section'),
        ),
    ]
