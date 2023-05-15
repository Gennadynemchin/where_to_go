from django.contrib import admin
from django.urls import path
from where_to_go.views import index, place_detail
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('<int:place>/', place_detail, name='place_detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
