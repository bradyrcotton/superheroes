from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from.models import Superhero

# Create your views here.


def index(request):
    all_superheros = Superhero.objects.all()
    context = {
        'all_superheros': all_superheros
    }
    return render(request, 'Superheros/index.html',context)


def detail(request, superhero_id):
    superhero = Superhero.objects.get(pk=superhero_id)
    context = {
        'superheros': superhero
    }
    return render(request, 'Superheros/detail.html', context)


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary_superhero_ability = request.POST.get('primary_superhero_ability')
        secondary_superhero_ability = request.POST.get('secondary_superhero_ability')
        catch_phrase = request.POST.get('catch_phrase')
        new_superhero = Superhero(name=name, alter_ego=alter_ego, primary_superhero_ability=primary_superhero_ability, secondary_superhero_ability=secondary_superhero_ability, catch_phrase=catch_phrase)
        new_superhero.save()
        return HttpResponseRedirect(reverse('Superheros:index'))
    else:
        return render(request, 'Superheros/create.html')
