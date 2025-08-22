from django.db import models

# Create your models here.
class Persona(models.Model):
    id_persona = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'persona'


class Tipo(models.Model):
    id_tipo = models.IntegerField(primary_key=True)
    cargo = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'tipo'


class Usuario(models.Model):
    pk = models.CompositePrimaryKey('id_persona', 'id_tipo')
    id_persona = models.ForeignKey(Persona, models.DO_NOTHING, db_column='id_persona')
    id_tipo = models.ForeignKey(Tipo, models.DO_NOTHING, db_column='id_tipo')
    usuario = models.CharField(max_length=45)
    pass_field = models.CharField(db_column='pass', max_length=45)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'usuario'