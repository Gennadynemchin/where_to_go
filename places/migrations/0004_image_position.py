# Generated by Django 4.2.1 on 2023-05-15 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_alter_image_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='position',
            field=models.IntegerField(db_index=True, default=0),
        ),
    ]
