from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),  #the path for our index view
]
