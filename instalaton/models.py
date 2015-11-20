from django.db import models
from django.utils import timezone

# Create your models here.
class Equipo(models.Model):
    serial = models.CharField("Serial",primary_key=True,max_length=200)
    usuario = models.ForeignKey('Usuario',related_name='Usuario',default="")
    sOActual = models.ForeignKey('SODisponible',related_name='Sistema_Operativo_Actual',default='')
    computador = models.CharField(max_length=200,null=True)
    marca = models.CharField(max_length=200,null=True)
    contrasena = models.CharField("Contrasena",max_length=200,null=True)
    ram = models.IntegerField("RAM", default = 0);
    backup = models.BooleanField("Backup",default=False)
    espacioSO = models.IntegerField("Espacio Sistema Operativo" , default=0);
    caracteristicas = models.CharField("caracteristicas",max_length=200,null=True)
    sOFuturo = models.ForeignKey('SODisponible', related_name='Sistema_Operativo_Futuro',default='' )

class Usuario(models.Model):
    documento = models.CharField("Documento", primary_key=True,max_length=20)
    nombre = models.CharField("Nombre" , max_length=200,null=True)
    correo = models.CharField("Correo" , max_length=100,null=True)
    celular = models.IntegerField("Numero Celular",default=0)
    tipoDocumento = models.CharField("Tipo Documento",max_length=4)
    semestre = models.IntegerField("Semestre",default=0)
    carrera  = models.CharField("Carrera",max_length=120,null=True) 
    username = models.CharField("Nick", max_length = 100,null=True)
    contrasena = models.CharField("Contrasena",max_length=100,null=True)
    rol = models.CharField("Rol", max_length = 100,null=True)
    
class SODisponible(models.Model):
    nombre = models.CharField(max_length=200, primary_key = True)
    version = models.CharField(max_length=200,null=True)
    arquitectura = models.CharField(max_length=200,null=True)
    espacio_requerido_gb = models.CharField(max_length=200,null=True)


class Entrega(models.Model):
    id_entrega = models.CharField("no de entrega", primary_key=True,max_length=200)
    equipo = models.ForeignKey('Equipo', related_name='Equipo',default='')
    usuario =  models.ForeignKey('Usuario' , related_name='Dueno',default='')
    organizador = models.ForeignKey('Usuario',related_name='Organizador',default='')
    fecha = models.DateTimeField(default=timezone.now,null = True)
    observaciones = models.CharField("Observaciones",max_length=200,null = True)
    instalador = models.ForeignKey('Usuario',related_name='instalador', default='')
    estado  = models.CharField("Estado",max_length=200,null = True)
    
    