# Generated by Django 4.1.1 on 2022-10-22 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_alter_inner_image_alter_section_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.FileField(blank=True, null=True, upload_to='mainsections')),
            ],
        ),
    ]
