# Generated by Django 4.2.1 on 2023-05-21 16:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("places", "0008_alter_image_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="place",
            name="description_short",
            field=models.TextField(verbose_name="Description"),
        ),
    ]
