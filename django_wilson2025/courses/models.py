# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

# Create your models here.
class TblCategoria(models.Model):
    categoria_id = models.AutoField(primary_key=True)
    categoria_nombre = models.CharField(max_length=200)

    class Meta:
        managed = True
        db_table = 'tbl_categoria'
    #Esto par que lo convierta a strings y no objetos de django 
    def __str__(self):
        return self.categoria_nombre

class TblCurso(models.Model):
    curso_id = models.AutoField(primary_key=True)
    curso_titulo = models.CharField(max_length=255)
    curso_descripcion = models.TextField()
    categoria = models.ForeignKey(TblCategoria, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'tbl_curso'
    
    def __str__(self):
        return self.curso_titulo
       