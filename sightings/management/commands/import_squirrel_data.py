import csv
import datetime

from django.core.management.base import BaseCommand

from sightings.models import Sight

from distutils.util import strtobool


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *args, **options):
        Sight.objects.all().delete()   #Deleting dummy squirrels before importing
        with open(options['csv_file']) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)
           # print(data)

        for item in data:
           # print(f'reading {item}')
            s = Sight(
                Longitude=item['X'],
                Latitude=item['Y'],
                Shift=item['Shift'],
                Date = datetime.datetime.strptime(item['Date'],'%m%d%Y'),
                Unique_Squirrel_Id=item['Unique Squirrel ID'],
                Age=item['Age'],
                Primary_Fur_Color=item['Primary Fur Color'],
                Location=item['Location'],
                Specific_Location=item['Specific Location'],
                Running=strtobool(item['Running']),
                Chasing=strtobool(item['Chasing']),
                Climbing=strtobool(item['Climbing']),
                Eating=strtobool(item['Eating']),
                Foraging=strtobool(item['Foraging']),
                Other_Activities=item['Other Activities'],
                Kuks=strtobool(item['Kuks']),
                Quaas=strtobool(item['Quaas']),
                Moans=strtobool(item['Moans']),
                Tail_Flags=strtobool(item['Tail flags']),
                Tail_Twitches=strtobool(item['Tail twitches']),
                Approaches=strtobool(item['Approaches']),
                Indifferent=strtobool(item['Indifferent']),
                Runs_From=strtobool(item['Runs from']),
            )
            s.save()
           # print(f'read {item}')
