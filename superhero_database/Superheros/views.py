from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from.models import Superhero
from django.urls import reverse

# Create your views here.


def index(request):
    all_superheros = Superhero.objects.all()
    context = {
        'all_superheros': all_superheros
    }
    return render(request, 'Superheros/index.html',context)


def detail(request, superhero_id):
    one_superhero = Superhero.objects.get(pk=superhero_id)
    return render(request, 'Superheros/index.html', one_superhero)


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        universe = request.POST.get('universe')
        powers = request.POST.get('powers')
        new_superhero = Superhero(name=name, universe=universe, powers=powers)
        new_superhero.save()
        return HttpResponseRedirect(reverse('Superheros:index'))
    else:
        return render(request, 'Superheros/create.html')
