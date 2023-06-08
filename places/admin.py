from adminsortable2.admin import SortableAdminBase
from adminsortable2.admin import SortableStackedInline
from django.contrib import admin
from django.utils.html import format_html

from .models import Image
from .models import Place


class ImageStackedInline(SortableStackedInline):
    model = Image
    readonly_fields = ["get_image_preview"]

    def get_image_preview(self, img):
        return format_html("<img src = {} height = '200'/>", img.image.url)


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ["title"]
    inlines = [ImageStackedInline]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = (
        "image",
        "position",
        "place",
    )
