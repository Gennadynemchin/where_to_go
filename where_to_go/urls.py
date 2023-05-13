from django.contrib import admin
from django.urls import path
from where_to_go.views import blank_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blank_page)
]
