from django.forms import ModelForm, TextInput
from .models import City
from mood.models import Mood

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'}),
        } #updates the input class to have the correct Bulma class and placeholder

class MoodForm(ModelForm):
    class Meta:
        model = Mood
        fields = ['mood']
        widgets = {
            'name': TextInput(attrs={'class' : 'input', 'placeholder' : 'Feeling...'}),
        } #updates the input class to have the correct Bulma class and placeholder
