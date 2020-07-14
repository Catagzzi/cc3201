from django import forms
from .models import Region

class Query1(forms.Form):
    nombre = forms.CharField(label="Pon tu nonbre aqui pls")
    curso = forms.IntegerField(label="Curso")

class RegionForm(forms.Form):
    choices = [(region.codigo, region.nombre) for region in Region.objects.filter()]
    codigo = forms.ChoiceField(label="Codigo de región", choices=choices)
