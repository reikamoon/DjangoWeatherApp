from django.forms import ModelForm, TextInput
from .models import Mood

class MoodForm(ModelForm):
    class Meta:
        model = Mood
        fields = ['mood']
        widgets = {
            'name': TextInput(attrs={'class' : 'input', 'placeholder' : 'Feeling...'}),
        } #updates the input class to have the correct Bulma class and placeholder
