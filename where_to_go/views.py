from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse

from places.models import Place


def place_detail(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    details = {
        "title": place.title,
        "imgs": [image.image.url for image in place.images.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {"lng": place.lon, "lat": place.lat},
    }
    return JsonResponse(
        details, safe=False, json_dumps_params={"ensure_ascii": False, "indent": 2}
    )


def index(request):
    places = Place.objects.all()
    features = []
    for place in places:
        features.append(
            {
                "type": "Feature",
                "geometry": {"type": "Point", "coordinates": [place.lon, place.lat]},
                "properties": {
                    "title": place.title,
                    "placeId": place.id,
                    "detailsUrl": reverse("places", kwargs={"place_id": place.id}),
                },
            }
        )
    context = {"places": {"type": "FeatureCollection", "features": features}}
    return render(request, "index.html", context)
