import csv
import datetime
from django.core.management.base import BaseCommand
from sightings.models import Sight

class Command(BaseCommand):
    def add_arguments(self,parser):
        parser.add_argument('csv_file')

    def handle(self, *args, **options):
        with open(options['csv_file']) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)
        
        def convertBool(str_):
            if str(str_) in ['TRUE', 'true', 'True']:
                str_ = True
            elif str(str_) in ['FALSE', 'false', 'False']:
                str_ = False
            else:
                str_ = None
            return str_

        for item in data:
            s = Sight(
                    Longitude = item['X'],
                    Latitude = item['Y'],
                    Unique_Squirrel_Id = item['Unique Squirrel ID'],
                    Shift = item['Shift'],
                    Date = datetime.datetime.strptime(item['Date'],'%m%d%Y'),
                    Age = item['Age'],
                    Primary_Fur_Color = item['Primary Fur Color'],
                    Location = item['Location'],
                    Specific_Location = item['Specific Location'],
                    Running = convertBool(item['Running']),
                    Chasing = convertBool(item['Chasing']),
                    Climbing = convertBool(item['Climbing']),
                    Eating = convertBool(item['Eating']),
                    Foraging = convertBool(item['Foraging']),
                    Other_Activities = item['Other Activities'],
                    Kuks = convertBool(item['Kuks']),
                    Quaas = convertBool(item['Quaas']),
                    Moans = convertBool(item['Moans']),
                    Tail_Flags = convertBool(item['Tail flags']),
                    Tail_Twitches = convertBool(item['Tail twitches']),
                    Approaches = convertBool(item['Approaches']),
                    Indifferent = convertBool(item['Indifferent']),
                    Runs_From = convertBool(item['Runs from']),
                    )
            s.save()

