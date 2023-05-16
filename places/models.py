from django.db import models
from django.utils.html import mark_safe
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Title', max_length=200)
    description_short = models.CharField('Description', max_length=300)
    description_long = HTMLField('Full description')
    lat = models.FloatField(verbose_name='Latitude')
    lon = models.FloatField(verbose_name='Longitude')

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField()
    position = models.PositiveIntegerField(default=0, db_index=True)
    place = models.ForeignKey(Place, verbose_name='Place', on_delete=models.CASCADE, related_name='images')

    class Meta:
        ordering = ['position']

    def image_preview(self):
        return mark_safe(f'<img src = "{self.image.url}" width = "150"/>')


    def __str__(self):
        return self.place.title
