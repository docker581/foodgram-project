from django.core.management.base import BaseCommand

from data.models import Ingredient
from foodgram_project.settings import BASE_DIR

import os
import csv

CSV_FILE_PATH = os.path.join(BASE_DIR, 'ingredients.csv')


class Command(BaseCommand):
    help = 'Load ingredients.csv'

    def handle(self, *args, **options):
        with open(CSV_FILE_PATH, encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                name, dimension = row
                Ingredient.objects.get_or_create(
                    name=name,
                    dimension=dimension,
                )
