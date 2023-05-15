from django.shortcuts import render
from places.models import Place, Image
from django.http import JsonResponse


def place_detail(request, place):
    place = Place.objects.get(pk=place)
    details = {
        "title": place.title,
        "imgs": [image.image.url for image in place.images.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": str(place.lon),
            "lat": str(place.lat)
        }
    }
    return JsonResponse(details, safe=False)


def index(request):
    places = Place.objects.all()
    features = []
    for place in places:
        title = place.title
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
                "placeId": place.id,
                "detailsUrl": place.id
            }
        })
    context = {"places": {
        "type": "FeatureCollection",
        "features": features
    }}
    return render(request, 'index.html', context)
