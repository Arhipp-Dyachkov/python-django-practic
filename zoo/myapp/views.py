from django.shortcuts import render
from django.http import HttpResponse
from .models import Animals


def index(request):
    animal = Animals.objects.all()
    return render(request, 'zoo.html', {'animals': animal})


def single_animal(request, animal_id):
    animal = Animals.objects.get(pk=animal_id)
    return render(request, 'single_animal.html', {'animal': animal})
