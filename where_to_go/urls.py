from django.contrib import admin
from django.urls import path
from where_to_go.views import index
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
