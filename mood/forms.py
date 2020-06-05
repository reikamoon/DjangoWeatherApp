from django.forms import ModelForm, TextInput
from .models import Mood

class MoodForm(ModelForm):
    class Meta:
        model = Mood
        fields = ['mood']
