import requests
from time import time
from PIL import Image as Image_saver
from io import BytesIO
from places.models import Place, Image
from django.core.management.base import BaseCommand, CommandError
from django.core.files.base import ContentFile



class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('download_link', nargs='+', type=str)

    def handle(self, *args, **options):
        response = requests.get(options['download_link'][0])
        response.raise_for_status()
        content = response.json()
        images = content['imgs']

        new_place = Place.objects.create(title=content['title'],
                                         description_short=content['description_short'],
                                         description_long=content['description_long'],
                                         lat=content['coordinates']['lat'],
                                         lon=content['coordinates']['lng'])
        for image_url in images:
            image_request = requests.get(image_url)
            image_request.raise_for_status()
            # image = Image_saver.open(BytesIO(image_request.content))
            new_image = Image.objects.create(position=1, place=new_place)
            new_image.image.save(content=ContentFile(image_request.content), name=str(time()), save=True)
            self.stdout.write(self.style.SUCCESS('Successfully saved'))
