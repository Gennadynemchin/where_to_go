# Generated by Django 4.2.1 on 2023-05-15 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_image_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='position',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
    ]
