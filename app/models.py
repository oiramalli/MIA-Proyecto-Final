# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

class Admin(models.Model):
    nombre = models.CharField(max_length=200, blank=True, null=True)
    eslogan = models.CharField(max_length=600, blank=True, null=True)
    imagen_logo = models.TextField(blank=True, null=True)  # This field type is a guess.
    video = models.TextField(blank=True, null=True)  # This field type is a guess.
    mision = models.CharField(max_length=2000, blank=True, null=True)
    vision = models.CharField(max_length=2000, blank=True, null=True)
    acerca = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin'


class Bitacora(models.Model):
    id_bit = models.BigIntegerField(primary_key=True)
    fecha = models.DateField()
    usuario_id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_id_usuario')
    elemento_id_elemento = models.ForeignKey('Elemento', models.DO_NOTHING, db_column='elemento_id_elemento')

    class Meta:
        managed = False
        db_table = 'bitacora'

class Chat(models.Model):
    id_chat = models.BigIntegerField(primary_key=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    usuario_admin = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_admin',related_name='%(class)s_usuario_admin')
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario')

    class Meta:
        managed = False
        db_table = 'chat'

class Elemento(models.Model):
    id_elemento = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=1)
    data = models.BinaryField(blank=True, null=True)
    elementop = models.ForeignKey('self', models.DO_NOTHING, db_column='elementop', blank=True, null=True)
    permisos = models.BigIntegerField(blank=True, null=True)
    grupo_id_grupo = models.ForeignKey('Grupo', models.DO_NOTHING, db_column='grupo_id_grupo')
    usuario_id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_id_usuario')

    class Meta:
        managed = False
        db_table = 'elemento'

class Grupo(models.Model):
    id_grupo = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'grupo'

class Mensaje(models.Model):
    id_mensaje = models.BigIntegerField(primary_key=True)
    emisor = models.CharField(max_length=200)
    fecha = models.DateField(blank=True, null=True)
    mensaje = models.CharField(max_length=2000, blank=True, null=True)
    chat_id_chat = models.ForeignKey(Chat, models.DO_NOTHING, db_column='chat_id_chat')

    class Meta:
        managed = False
        db_table = 'mensaje'

class Usuario(models.Model):
    id_usuario = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    telefono = models.BigIntegerField()
    direccion = models.CharField(max_length=600)
    clave = models.CharField(max_length=32)
    correo = models.CharField(max_length=100)
    foto = models.TextField()  # This field type is a guess.
    genero = models.CharField(max_length=40)
    fecha_nacimiento = models.DateField()
    fecha_registro = models.DateField()
    estatus = models.CharField(max_length=1)
    estatus_cuenta = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'usuario'

class UsuarioGrupo(models.Model):
    usuario_id_usuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='usuario_id_usuario')
    grupo_id_grupo = models.ForeignKey(Grupo, models.DO_NOTHING, db_column='grupo_id_grupo')

    class Meta:
        managed = False
        db_table = 'usuario_grupo'
