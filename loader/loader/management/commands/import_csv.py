import csv
from django.core.management.base import BaseCommand
from loader.models import TestModel

class Command(BaseCommand):
    help = 'Load a list of data from a CSV file into the TestModel table'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file to load')

    def handle(self, *args, **options):
        with open(options['csv_file'], newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                TestModel.objects.create(
                    field1=row['field1'],
                    field2=row['field2']
                )
