# Generated by Django 4.2.1 on 2023-05-16 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0007_alter_place_description_long'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
