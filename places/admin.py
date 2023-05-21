from django.contrib import admin
from .models import Place, Image
from django.utils.html import mark_safe
from adminsortable2.admin import SortableStackedInline, SortableAdminBase


class ImageStackedInline(SortableStackedInline):
    model = Image
    readonly_fields = ["image_preview"]

    def image_preview(self, obj):
        return mark_safe(f'<img src = "{obj.image.url}" height = "150"/>')


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
