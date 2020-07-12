# This is an auto-generated Django model module.
# python manage.py inspectdb > /home/catalina/Documents/septimo_semestre_electrica/Bases_de_Datos/cc3201/applications/rendimientos/models.py
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Colegios(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    comuna = models.ForeignKey('Comuna', models.DO_NOTHING, db_column='comuna', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'colegios'


class Comuna(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comuna'


class Enseanza(models.Model):
    codigo = models.IntegerField(primary_key=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enseñanza'


class Idps(models.Model):
    colegio = models.ForeignKey(Colegios, models.DO_NOTHING, db_column='colegio', blank=True, null=True)
    agno = models.IntegerField(blank=True, null=True)
    grado = models.CharField(max_length=255, blank=True, null=True)
    ind_am = models.FloatField(blank=True, null=True)
    ind_cc = models.FloatField(blank=True, null=True)
    ind_pf = models.FloatField(blank=True, null=True)
    ind_hv = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'idps'


class Provincia(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'provincia'


class Region(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'region'


class Rendimientos(models.Model):
    agno = models.IntegerField(primary_key=True)
    codigo = models.ForeignKey(Region, models.DO_NOTHING, db_column='codigo')
    digito_verificador = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    region = models.ForeignKey(Region, models.DO_NOTHING, db_column='region', blank=True, null=True)
    provincia = models.ForeignKey(Provincia, models.DO_NOTHING, db_column='provincia', blank=True, null=True)
    comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='comuna', blank=True, null=True)
    cod_depe2 = models.IntegerField(blank=True, null=True)
    rural_rbd = models.IntegerField(blank=True, null=True)
    cod_ense = models.IntegerField()
    apr_hom_01 = models.IntegerField(blank=True, null=True)
    apr_hom_02 = models.IntegerField(blank=True, null=True)
    apr_hom_03 = models.IntegerField(blank=True, null=True)
    apr_hom_04 = models.IntegerField(blank=True, null=True)
    apr_hom_05 = models.IntegerField(blank=True, null=True)
    apr_hom_06 = models.IntegerField(blank=True, null=True)
    apr_hom_07 = models.IntegerField(blank=True, null=True)
    apr_hom_08 = models.IntegerField(blank=True, null=True)
    apr_muj_01 = models.IntegerField(blank=True, null=True)
    apr_muj_02 = models.IntegerField(blank=True, null=True)
    apr_muj_03 = models.IntegerField(blank=True, null=True)
    apr_muj_04 = models.IntegerField(blank=True, null=True)
    apr_muj_05 = models.IntegerField(blank=True, null=True)
    apr_muj_06 = models.IntegerField(blank=True, null=True)
    apr_muj_07 = models.IntegerField(blank=True, null=True)
    apr_muj_08 = models.IntegerField(blank=True, null=True)
    rep_hom_01 = models.IntegerField(blank=True, null=True)
    rep_hom_02 = models.IntegerField(blank=True, null=True)
    rep_hom_03 = models.IntegerField(blank=True, null=True)
    rep_hom_04 = models.IntegerField(blank=True, null=True)
    rep_hom_05 = models.IntegerField(blank=True, null=True)
    rep_hom_06 = models.IntegerField(blank=True, null=True)
    rep_hom_07 = models.IntegerField(blank=True, null=True)
    rep_hom_08 = models.IntegerField(blank=True, null=True)
    rep_muj_01 = models.IntegerField(blank=True, null=True)
    rep_muj_02 = models.IntegerField(blank=True, null=True)
    rep_muj_03 = models.IntegerField(blank=True, null=True)
    rep_muj_04 = models.IntegerField(blank=True, null=True)
    rep_muj_05 = models.IntegerField(blank=True, null=True)
    rep_muj_06 = models.IntegerField(blank=True, null=True)
    rep_muj_07 = models.IntegerField(blank=True, null=True)
    rep_muj_08 = models.IntegerField(blank=True, null=True)
    ret_hom_01 = models.IntegerField(blank=True, null=True)
    ret_hom_02 = models.IntegerField(blank=True, null=True)
    ret_hom_03 = models.IntegerField(blank=True, null=True)
    ret_hom_04 = models.IntegerField(blank=True, null=True)
    ret_hom_05 = models.IntegerField(blank=True, null=True)
    ret_hom_06 = models.IntegerField(blank=True, null=True)
    ret_hom_07 = models.IntegerField(blank=True, null=True)
    ret_hom_08 = models.IntegerField(blank=True, null=True)
    ret_muj_01 = models.IntegerField(blank=True, null=True)
    ret_muj_02 = models.IntegerField(blank=True, null=True)
    ret_muj_03 = models.IntegerField(blank=True, null=True)
    ret_muj_04 = models.IntegerField(blank=True, null=True)
    ret_muj_05 = models.IntegerField(blank=True, null=True)
    ret_muj_06 = models.IntegerField(blank=True, null=True)
    ret_muj_07 = models.IntegerField(blank=True, null=True)
    ret_muj_08 = models.IntegerField(blank=True, null=True)
    tra_hom_01 = models.IntegerField(blank=True, null=True)
    tra_hom_02 = models.IntegerField(blank=True, null=True)
    tra_hom_03 = models.IntegerField(blank=True, null=True)
    tra_hom_04 = models.IntegerField(blank=True, null=True)
    tra_hom_05 = models.IntegerField(blank=True, null=True)
    tra_hom_06 = models.IntegerField(blank=True, null=True)
    tra_hom_07 = models.IntegerField(blank=True, null=True)
    tra_hom_08 = models.IntegerField(blank=True, null=True)
    tra_muj_01 = models.IntegerField(blank=True, null=True)
    tra_muj_02 = models.IntegerField(blank=True, null=True)
    tra_muj_03 = models.IntegerField(blank=True, null=True)
    tra_muj_04 = models.IntegerField(blank=True, null=True)
    tra_muj_05 = models.IntegerField(blank=True, null=True)
    tra_muj_06 = models.IntegerField(blank=True, null=True)
    tra_muj_07 = models.IntegerField(blank=True, null=True)
    tra_muj_08 = models.IntegerField(blank=True, null=True)
    si_hom_01 = models.IntegerField(blank=True, null=True)
    si_hom_02 = models.IntegerField(blank=True, null=True)
    si_hom_03 = models.IntegerField(blank=True, null=True)
    si_hom_04 = models.IntegerField(blank=True, null=True)
    si_hom_05 = models.IntegerField(blank=True, null=True)
    si_hom_06 = models.IntegerField(blank=True, null=True)
    si_hom_07 = models.IntegerField(blank=True, null=True)
    si_hom_08 = models.IntegerField(blank=True, null=True)
    si_muj_01 = models.IntegerField(blank=True, null=True)
    si_muj_02 = models.IntegerField(blank=True, null=True)
    si_muj_03 = models.IntegerField(blank=True, null=True)
    si_muj_04 = models.IntegerField(blank=True, null=True)
    si_muj_05 = models.IntegerField(blank=True, null=True)
    si_muj_06 = models.IntegerField(blank=True, null=True)
    si_muj_07 = models.IntegerField(blank=True, null=True)
    si_muj_08 = models.IntegerField(blank=True, null=True)
    prom_asis_apr_hom = models.CharField(max_length=255, blank=True, null=True)
    prom_asis_apr_muj = models.CharField(max_length=255, blank=True, null=True)
    prom_asis_rep_hom = models.CharField(max_length=255, blank=True, null=True)
    prom_asis_rep_muj = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rendimientos'
        unique_together = (('agno', 'codigo', 'cod_ense'),)
