from django import forms
from .models import Region, Colegios, Rendimientos, RendimientoCurso

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

class RendimientosForm(forms.Form):
    choices1 = [(colegio.nombre, colegio.nombre) for colegio in Colegios.objects.filter().order_by('nombre')]
    nombre = forms.ChoiceField(label="Nombre de Colegio", choices=choices1)
    choices2 = [(Tipo.tipo_ensenanza, "Básica" if Tipo.tipo_ensenanza == 0 else "Media") for Tipo in RendimientoCurso.objects.filter().distinct('tipo_ensenanza')]
    tipo = forms.ChoiceField(label="Tipo de enseñanza", choices=choices2)
    choices3 = [(Tipo.nivel_ensenanza , Tipo.nivel_ensenanza) for Tipo in RendimientoCurso.objects.filter().distinct('nivel_ensenanza')]
    nivel = forms.ChoiceField(label="Curso(1-8 para basica, 1-4 para media", choices=choices3)

