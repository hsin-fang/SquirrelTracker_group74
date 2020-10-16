from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Sight(models.Model):
    Longitude  = models.FloatField(
            help_text = _('Longitude of the sight'),)

    Latitude = models.FloatField(
            help_text = _('Latitude of the sight'),)

    Unique_Squirrel_Id = models.CharField(
            help_text = _('The unique ID of the squirrel'),
            max_length = 25,
            )
    AM = 'AM'
    PM = 'PM'
    SESSION=(
            (AM,'AM'),
            (PM,'PM'),
            )

    Shift = models.CharField(
            help_text = _('Whether the sight is in the morning or late afternoon?'),
            max_length=16,
            choices=SESSION,
            blank=True)

    Date = models.DateField(
            help_text = _('The format is in yyyy-mm-dd'),
            null = True,
            blank=True)

    Adult = 'Adult'
    Juvenile = 'Juvenile'
    Unknown = '?'
    AGE_CHOICE=(
            (Adult,'Adult'),
            (Juvenile, 'Juvenile'),
            (None, ''),
            (Unknown, '?'),
            )

    Age = models.CharField(
            help_text = _('Age of the squirrel'),
            max_length=16,
            choices = AGE_CHOICE,
            blank = True
            )

    Black = 'Black'
    Gray = 'Gray'
    Cinnamon = 'Cinnamon'
    COLOR_CHOICE=(
            (Black, 'Black'),
            (Gray, 'Gray'),
            (Cinnamon, 'Cinnamon'),
            (None, ''),
            )

    Primary_Fur_Color = models.CharField(
            help_text = _('Fur color'),
            max_length=16,
            choices = COLOR_CHOICE,
            blank = True
            )

    Ground_Plane = 'Ground Plane'
    Above_Ground = 'Above Ground'
    LOCATION_CHOICE=(
            (Ground_Plane, 'Ground Plane'),
            (Above_Ground, 'Above Ground'),
            (None, ''),
            )
    
    Location =  models.CharField(
            help_text = _('Location'),
            max_length=128,
            choices = LOCATION_CHOICE,
            blank = True
            )

    Specific_Location = models.CharField(
            help_text = _('Additional notes to the location'),
            max_length=128,
            blank = True,
            )

    Running = models.NullBooleanField(
            help_text = _('Running'),
            blank=True,
    )
    
    Chasing = models.NullBooleanField(
            help_text = _('Chasing'),
            blank=True,
    )

    Climbing = models.NullBooleanField(
            help_text = _('Climbing'),
            blank=True,
    )

    Eating = models.NullBooleanField(
            help_text = _('Eating'),
            blank=True,
    )

    Foraging = models.NullBooleanField(
            help_text = _('Foraging'),
            blank=True,
    )

    Other_Activities = models.CharField(
        help_text = _('Other Activities'),
        max_length = 128,
        null = True,
        blank = True
    )

    Kuks = models.NullBooleanField(
            help_text = _('Kuks'),
            blank=True,
    )

    Quaas = models.NullBooleanField(
            help_text = _('Quaas'),
            blank=True,
    )

    Moans = models.NullBooleanField(
            help_text = _('Moans'),
            blank=True,
    )

    Tail_Flags = models.NullBooleanField(
            help_text = _('Tail_Flags'),
            blank=True,
    )

    Tail_Twitches = models.NullBooleanField(
            help_text = _('Tail_Twitches'),
            blank=True,
    )

    Approaches = models.NullBooleanField(
            help_text = _('Approaches'),
            blank=True,
    )

    Indifferent = models.NullBooleanField(
            help_text = _('Indifferent'),
            blank=True,
    )
    
    Runs_From = models.NullBooleanField(
            help_text = _('Runs_From'),
            blank=True,
    )
