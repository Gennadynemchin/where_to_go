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
        try:
            images = content["imgs"]
            new_place, created = Place.objects.get_or_create(
                title=content["title"],
                description_short=content["description_short"],
                description_long=content["description_long"],
                lat=content["coordinates"]["lat"],
                lon=content["coordinates"]["lng"],
            )
            self.stdout.write(
                self.style.SUCCESS(f'Successfully saved place {content["title"]}')
            )

            for image_count, image_url in enumerate(images):
                image_request = requests.get(image_url)
                image_request.raise_for_status()
                image_file = ContentFile(image_request.content)
                image_name = os.path.basename(urlparse(image_url).path)
                new_image, created = Image.objects.get_or_create(
                    position=image_count, place=new_place
                )
                new_image.image.save(content=image_file, name=image_name, save=True)
                self.stdout.write(
                    self.style.SUCCESS(
                        f'Successfully saved image {image_name} for place {content["title"]}'
                    )
                )
        except KeyError:
            self.stdout.write(self.style.WARNING("Wrong JSON format!"))
