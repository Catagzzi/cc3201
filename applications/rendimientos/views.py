from django.shortcuts import render
from .models import Region, Rendimientos, RendimientoCurso, Idps
from .forms import   AsistenciaForm, RendimientosForm, CursosForm, IdpsForm
from django.http import HttpResponseRedirect


def home(request):
    return render(request, 'home/home.html')



def asistencias(request):
    if request.method == 'POST':
        form = AsistenciaForm(request.POST)
        codigo = form.data['codigo']
        anho = form.data['anho']
        query = """SELECT  digito_verificador, nombre, agno, codigo, cod_ense, 
        prom_asis_apr_hom, prom_asis_apr_muj, prom_asis_rep_hom, prom_asis_rep_muj 
        FROM rendimientos2 WHERE codigo=%s AND agno=%s"""
        asistencias = Rendimientos.objects.raw(query, [codigo,anho])
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
        query = """SELECT id, cd.codigo as codigo, cd.nombre as nombre,
        cd.comuna_nombre as comuna, agno, curso, apr_hom, apr_muj 
        FROM rendimiento_curso rc 
        JOIN colegios_detalle cd ON rc.codigo = cd.codigo
        WHERE tipo_ensenanza = %s
        AND nivel_ensenanza = %s 
        AND cd.nombre LIKE (%s);"""
        rendimientos = RendimientoCurso.objects.raw(query, [tipo,nivel,nombre])
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


def cursos(request):
    if request.method == 'POST':
        form = CursosForm(request.POST)
        nombre = form.data['nombre']
        query = """SELECT cd.codigo as codigo, cd.nombre as nombre,
        cd.comuna_codigo as comuna, agno as id,
        ROUND(SUM(rc.apr_hom*rc.n_apr_hom)/NULLIF(SUM(rc.n_apr_hom), 0), 3) as aprhom,
        ROUND(SUM(rc.apr_muj*rc.n_apr_muj)/NULLIF(SUM(rc.n_apr_muj), 0), 3) as aprmuj
        FROM rendimiento_curso rc
        JOIN colegios_detalle cd ON rc.codigo = cd.codigo
        WHERE cd.nombre LIKE %s
        GROUP BY cd.codigo, cd.nombre, cd.comuna_codigo, agno;"""
        rends_cursos = RendimientoCurso.objects.raw(query, [nombre])
        context = {
            'rendimientos': rends_cursos,
            'nombre': nombre
        }
        return render(request, 'rendimientos/rendimientos_cursos.html', context)
    else:
        form = CursosForm()
        nombre_form = "Formulario Rendimientos"
        context = {
            'form': form,
            'nombre_form': nombre_form
        }
        return render(request, 'rendimientos/cursos_form.html', context)



def idps(request):
    if request.method == 'POST':
        form = IdpsForm(request.POST)
        nombre = form.data['nombre']
        anho = form.data['anho']
        query = """SELECT cd.codigo as codigo, cd.nombre as nombre,
        cd.comuna_nombre as comuna, agno, grado,
        ind_am ,
        ind_cc ,
        ind_pf ,
        ind_hv 
        FROM idps JOIN colegios_detalle cd ON cd.codigo = idps.colegio
        WHERE cd.nombre LIKE %s 
        AND agno= %s ;"""
        idps_s = Idps.objects.raw(query, [nombre,anho])
        context = {
            'idps_s': idps_s,
            'nombre': nombre,
            'anho': anho
        }
        return render(request, 'rendimientos/idps.html', context)
    else:
        form = IdpsForm()
        nombre_form = "Formulario idps"
        context = {
            'form': form,
            'nombre_form': nombre_form
        }
        return render(request, 'rendimientos/idps_form.html', context)