from django import forms
from .models import Region, Colegios, Rendimientos

class Query1(forms.Form):
    nombre = forms.CharField(label="Pon tu nonbre aqui pls")
    curso = forms.IntegerField(label="Curso")

class RegionForm(forms.Form):
    choices = [(region.codigo, region.nombre) for region in Region.objects.filter()]
    codigo = forms.ChoiceField(label="Codigo de región", choices=choices)

class AsistenciaForm(forms.Form):
    choices1 = [(colegio.codigo, colegio.nombre) for colegio in Colegios.objects.filter().order_by('nombre')]
    codigo = forms.ChoiceField(label="Nombre de Colegio", choices=choices1)
    choices2 = [(año, año) for año in range(2014, 2018)]
    anho = forms.ChoiceField(label="Año", choices=choices2)

