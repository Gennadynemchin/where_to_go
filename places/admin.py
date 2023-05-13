from django.contrib import admin
from .models import Place



admin.site.register(Place)

'''
@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin)
'''