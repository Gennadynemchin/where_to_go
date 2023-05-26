from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField("Title", max_length=200)
    description_short = models.TextField("Description", blank=True)
    description_long = HTMLField("Full description", blank=True)
    lat = models.FloatField(verbose_name="Latitude")
    lon = models.FloatField(verbose_name="Longitude")

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField()
    position = models.PositiveIntegerField(default=0, db_index=True)
    place = models.ForeignKey(
        Place, verbose_name="Place", on_delete=models.CASCADE, related_name="images"
    )

    class Meta:
        ordering = ["position"]

    def __str__(self):
        return str(self.id)
