from django.db import models

# Create your models here.



class Cliente(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    apellido_cliente = models.CharField(max_length=100)
    direccion_cliente = models.CharField(max_length=200)
    telefono_cliente = models.IntegerField()
    edad_cliente = models.IntegerField()
    cedula_cliente = models.IntegerField()
    correo_cliente = models.CharField(max_length=100)

class Compra(models.Model):
    auto_comprado = models.ForeignKey('Automovil', on_delete=models.CASCADE)
    nombre_comprador = models.CharField(max_length=100)
    apellido_comprador = models.CharField(max_length=100)

class Automovil(models.Model):
    modelo_auto = models.CharField(max_length=100)
    placas_auto = models.CharField(max_length=20)
    precio_auto = models.DecimalField(max_digits=10, decimal_places=2)
    color_auto = models.CharField(max_length=50)
    edad_auto = models.IntegerField()
    serie_auto = models.CharField(max_length=50)
    descripcion_auto = models.TextField()
    trasmision_auto = models.CharField(max_length=50)
    motor_auto = models.CharField(max_length=50)
    consumo_gasolina = models.DecimalField(max_digits=5, decimal_places=2)


    
    