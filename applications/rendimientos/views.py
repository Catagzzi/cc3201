from django.shortcuts import render
from .models import Region
from .forms import Query1, RegionForm
from django.http import HttpResponseRedirect


def query_1(request):
    if request.method == 'POST':
        form = Query1(request.POST)
        context = {}
        context['nombre'] = form.data['nombre']
        context['curso'] = form.data['curso']
        context['results'] = ['primero', 'segundo']
        return render(request, 'rendimientos/results.html', context)
    else:
        form = Query1()
        context = {}
        context['form'] = form
        context['results'] = ['primero', 'segundo']
        return render(request, 'home/home.html', context)


def region(request):
    if request.method == 'POST':
        form = RegionForm(request.POST)
        codigo = form.data['codigo']
        query = f"SELECT * FROM region WHERE codigo >= {codigo}"
        regiones = Region.objects.raw(query)
        # en python:
        # regiones = Region.objects.filter(codigo__gte=codigo)
        context = {
            'regiones': regiones,
            'codigo': codigo
        }
        return render(request, 'rendimientos/results.html', context)
    else:
        form = RegionForm()
        return render(request, 'rendimientos/region.html', {'form': form})