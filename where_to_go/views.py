from django.http import HttpResponse
from django.shortcuts import render
from places.models import Place, Image


def index(request):
    places = Place.objects.all()
    features = []
    for place in places:
        title = place.title
        description = place.description_short
        description_full = place.description_long
        lat = place.lat
        lon = place.lon

        features.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [lon, lat]
            },

            "properties": {
                "title": title,
                "placeId": "test",
                "detailsUrl": {}
            }

        })
    content = {
        "type": "FeatureCollection",
        "features": features
    }
    print(content)
    return render(request, 'index.html')
