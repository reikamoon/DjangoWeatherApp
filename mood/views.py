from django.shortcuts import render
import requests
from .models import Mood
from .forms import MoodForm
from .models import Mood as MoodModel

# Create your views here.
def mood(request):
    mood = Mood.objects.last()
    if request.method == 'POST':
        form2 = MoodForm(request.POST)
        if form2.is_valid():
            form2.save()
            print(mood)


    form2 = MoodForm()

    context = {'form2': form2, 'mood': mood}

    return render(request, 'weather/mood.html', context)
