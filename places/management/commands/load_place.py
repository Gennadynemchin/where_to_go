import os
import requests
from urllib.parse import urlparse
from places.models import Place, Image
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("download_link", nargs="+", type=str)

    def handle(self, *args, **options):
        response = requests.get(options["download_link"][0])
        response.raise_for_status()
        content = response.json()
        place_images = content.get("imgs", [])
        place_desc_short = content.get("description_short", "Short description should be filled out later")
        place_desc_long = content.get("description_long", "Full description should be filled out later")
        try:
            place_title = content["title"]
            place_lat = content["coordinates"]["lat"]
            place_lng = content["coordinates"]["lng"]
        except KeyError:
            self.stdout.write(self.style.WARNING("Wrong JSON format. The place will no be added to database."))
        else:
            place, created = Place.objects.get_or_create(
                title=place_title,
                description_short=place_desc_short,
                description_long=place_desc_long,
                lat=place_lat,
                lon=place_lng,
            )
            if place_images:
                for image_count, image_url in enumerate(place_images):
                    image_request = requests.get(image_url)
                    image_request.raise_for_status()
                    image_file = ContentFile(image_request.content)
                    image_name = os.path.basename(urlparse(image_url).path)
                    new_image, created = Image.objects.get_or_create(
                        position=image_count, place=place
                    )
                    new_image.image.save(content=image_file, name=image_name, save=True)
                    self.stdout.write(
                        self.style.SUCCESS(
                            f'Successfully saved image {image_name} for place {content["title"]}'
                        )
                    )
        self.stdout.write(
            self.style.SUCCESS(f'Successfully saved place {content["title"]}')
        )
