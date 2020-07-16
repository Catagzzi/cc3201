from django.shortcuts import render
from .models import Region, Rendimientos, RendimientoCurso
from .forms import Query1, RegionForm, AsistenciaForm, RendimientosForm
from django.http import HttpResponseRedirect


def home(request):
    return render(request, 'home/home.html')


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
        nombre_form = "Formulario Región"
        context = {
            'form': form,
            'nombre_form': nombre_form
        }
        return render(request, 'rendimientos/ingreso.html', context)

def asistencias(request):
    if request.method == 'POST':
        form = AsistenciaForm(request.POST)
        codigo = form.data['codigo']
        anho = form.data['anho']
        query = f"""SELECT  digito_verificador, nombre, agno, codigo, cod_ense, prom_asis_apr_hom, prom_asis_apr_muj, prom_asis_rep_hom, prom_asis_rep_muj 
        FROM rendimientos2 WHERE codigo={codigo} AND agno={anho}"""
        asistencias = Rendimientos.objects.raw(query)
        context = {
            'asistencias': asistencias,
            'codigo': codigo,
            'anho': anho
        }
        return render(request, 'rendimientos/colegio_anho.html', context)
    else:
        form = AsistenciaForm()
        nombre_form = "Formulario Asistencias"
        context = {
            'form': form,
            'nombre_form': nombre_form
        }
        return render(request, 'rendimientos/ingreso.html', context)


def rendimientos(request):
    if request.method == 'POST':
        form = RendimientosForm(request.POST)
        nombre = form.data['nombre']
        tipo = form.data['tipo']
        nivel = form.data['nivel']
        query = f"""SELECT id, cd.codigo as codigo, cd.nombre as nombre,
        cd.comuna_nombre as comuna, agno, curso, apr_hom, apr_muj 
        FROM rendimiento_curso rc 
        JOIN colegios_detalle cd ON rc.codigo = cd.codigo
        WHERE tipo_ensenanza = {tipo}
        AND nivel_ensenanza = {nivel} 
        AND cd.nombre LIKE ('{nombre}');"""
        rendimientos = RendimientoCurso.objects.raw(query)
        context = {
            'rendimientos': rendimientos,
            'nombre': nombre,
            'tipo': tipo,
            'nivel': nivel
        }
        return render(request, 'rendimientos/rendimientos.html', context)
    else:
        form = RendimientosForm()
        nombre_form = "Formulario Rendimientos"
        context = {
            'form': form,
            'nombre_form': nombre_form
        }
        return render(request, 'rendimientos/rendimientos_form.html', context)
