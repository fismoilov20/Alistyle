# Generated by Django 4.1.1 on 2022-10-21 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inner',
            name='image',
            field=models.FileField(null=True, upload_to='inner_sections'),
        ),
        migrations.AlterField(
            model_name='section',
            name='image',
            field=models.FileField(null=True, upload_to='sections'),
        ),
    ]
