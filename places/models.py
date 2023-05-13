from django.db import models


class Place(models.Model):
    title = models.CharField('Title', max_length=200)
    description_short = models.CharField('Description', max_length=300)
    description_long = models.TextField('Full description')
    lat = models.FloatField(verbose_name='Latitude')
    lon = models.FloatField(verbose_name='Longitude')

    def __str__(self):
        return self.title
