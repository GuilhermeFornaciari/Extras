from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import animal,habitat
# Create your views here.


def index(request):
    a_animals = animal.objects.all()
    a_habitats = habitat.objects.all()
    package = {'a_animals': a_animals, 'a_habitats': a_habitats}
    return render(request,"index.html",package)

def animaldetail(request, animal_id):
    anim = get_object_or_404(animal,pk=animal_id)
    animals = animal.objects.all()

    total_votes = 0
    for a in animals:
        total_votes += a.votes

    context = {'anim': anim, 'total_votes': total_votes} 
    return render(request,"detail.html",context)

def habitatview(request, habitat_id):
    habit = get_object_or_404(habitat,pk=habitat_id)
    context = {'habitat': habit} 
    return render(request,"habitat.html",context)

def voteanimal(request, animal_id):
    anim = get_object_or_404(animal,pk=animal_id)
    anim.votes += 1
    anim.save()
    return HttpResponseRedirect(reverse('animals:detail',args=[anim.id]))
    