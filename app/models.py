# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

class Curso(models.Model):
    id_curso = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'curso'

class DetalleCurso(models.Model):
    id_curso = models.BigIntegerField(primary_key=True)
    persona_id_usuario = models.ForeignKey('Persona', models.DO_NOTHING, db_column='persona_id_usuario')
    curso_id_curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='curso_id_curso')

    class Meta:
        managed = False
        db_table = 'detalle_curso'


class Persona(models.Model):
    id_usuario = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'persona'

