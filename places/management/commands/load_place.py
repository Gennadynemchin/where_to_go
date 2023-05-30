import os
from urllib.parse import urlparse
import requests
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from places.models import Place, Image


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("download_link", type=str)

    def handle(self, *args, **options):
        response = requests.get(options["download_link"])
        response.raise_for_status()
        content = response.json()
        place_images = content.get("imgs", [])
        place_desc_short = content.get("description_short", "")
        place_desc_long = content.get("description_long", "")
        try:
            place_title = content["title"]
            place_lat = content["coordinates"]["lat"]
            place_lng = content["coordinates"]["lng"]
        except KeyError:
            self.stdout.write(self.style.WARNING("Wrong JSON format."
                                                 " The place will not be added to database.")
                              )
            return

        place, created = Place.objects.get_or_create(
            title=place_title,
            defaults={"description_short": place_desc_short,
                      "description_long": place_desc_long,
                      "lat": place_lat,
                      "lon": place_lng}
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(f'Successfully saved place {content["title"]}')
            )
            for image_count, image_url in enumerate(place_images):
                image_request = requests.get(image_url)
                image_request.raise_for_status()
                image_name = os.path.basename(urlparse(image_url).path)
                image_file = ContentFile(image_request.content, name=image_name)
                new_image, created = Image.objects.get_or_create(
                    position=image_count, place=place, image=image_file
                )
                self.stdout.write(
                    self.style.SUCCESS(
                        f'Successfully saved image {image_name} for place {content["title"]}'
                    )
                )
        else:
            self.stdout.write(
                self.style.WARNING(f'The place {content["title"]}'
                                   f' has not been saved. Probably it`s already exists'
                                   )
            )


