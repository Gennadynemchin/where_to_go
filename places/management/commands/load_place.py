import os
from urllib.parse import urlparse

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Image
from places.models import Place


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("download_link", type=str)

    def get_place_content(self, place_link):
        response = requests.get(place_link)
        response.raise_for_status()
        return response.json()

    def save_place(self, content):
        place_images = content.get("imgs", [])
        place_desc_short = content.get("description_short", "")
        place_desc_long = content.get("description_long", "")
        try:
            place_title = content["title"]
            place_lat = content["coordinates"]["lat"]
            place_lng = content["coordinates"]["lng"]
        except KeyError:
            self.stdout.write(
                self.style.WARNING(
                    "Wrong JSON format." " The place will not be added to database."
                )
            )
            return
        place, created = Place.objects.get_or_create(
            title=place_title,
            defaults={
                "description_short": place_desc_short,
                "description_long": place_desc_long,
                "lat": place_lat,
                "lon": place_lng,
            },
        )
        return {
            "created": created,
            "place_images": place_images,
            "place_title": place_title,
            "place": place,
        }

    def save_images(self, place_images, place):
        for image_count, image_url in enumerate(place_images):
            image_request = requests.get(image_url)
            image_request.raise_for_status()
            image_name = os.path.basename(urlparse(image_url).path)
            image_file = ContentFile(image_request.content, name=image_name)
            Image.objects.create(position=image_count, place=place, image=image_file)
            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully saved image {image_name} for place {place.title}"
                )
            )
        return self.stdout.write(
            self.style.SUCCESS(f"All images for place {place.title} successfully saved")
        )

    def handle(self, *args, **options):
        place_content = self.get_place_content(options["download_link"])
        place_data = self.save_place(place_content)

        created = place_data["created"]
        place_images = place_data["place_images"]
        place_title = place_data["place_title"]
        place = place_data["place"]

        if not created:
            self.stdout.write(
                self.style.WARNING(
                    f"The place {place_title} has not been saved. Probably it`s already exists"
                )
            )
            return
        self.stdout.write(self.style.SUCCESS(f"Successfully saved place {place_title}"))
        self.save_images(place_images, place)
