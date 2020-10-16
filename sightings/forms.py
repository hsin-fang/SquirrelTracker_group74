from django.forms import ModelForm
from .models import Sight

class SightForm(ModelForm):
    class Meta:
        model = Sight
        fields = '__all__'
