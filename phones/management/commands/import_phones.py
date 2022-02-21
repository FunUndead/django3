import csv
from django.core.management.base import BaseCommand
from phones.models import Phone
from django.utils.text import slugify
8
class Command(BaseCommand):

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):

        path = r'\phones.csv'# путь к файлу
        with open(path, 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            # TODO: Добавьте сохранение модели
            p = Phone.objects.create(id = phone['id'], name = phone['name'], price = phone['price'],
                                 image = phone['image'], release_date = phone['release_date'], lte_exists = phone['lte_exists'], slug = slugify(phone['name']))

            p.save()

