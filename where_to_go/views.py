from django.shortcuts import render
from places.models import Place
from django.http import JsonResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404


def place_detail(request, place):
    place = get_object_or_404(Place, id=place)
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
    return JsonResponse(details, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 2})


def index(request):
    places = Place.objects.all()
    features = []
    for place in places:
        features.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lon, place.lat]
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": reverse('places', kwargs={'place': place.id})
            }
        })
    context = {"places": {
        "type": "FeatureCollection",
        "features": features
    }}
    return render(request, 'index.html', context)
