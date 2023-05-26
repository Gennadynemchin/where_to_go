from django.contrib import admin
from django.urls import path, include
from where_to_go.views import index, place_detail
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index),
    path("places/<int:place_id>/", place_detail, name="places"),
    path("tinymce/", include("tinymce.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
