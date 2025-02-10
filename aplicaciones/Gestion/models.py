from django.db import models

# Create your models here.
class Proyecto(models.Model):
    id = models.AutoField(primary_key=True)  # ID autoincremental
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)
    foto = models.FileField(upload_to='proyecto',null=True,blank=True)
    def __str__(self):
        return self.nombre

class ClienteVIP(models.Model):
    id = models.AutoField(primary_key=True)  # ID autoincremental
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Vivienda(models.Model):
    id = models.AutoField(primary_key=True)  # ID autoincremental
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name="viviendas")
    cliente = models.ForeignKey(ClienteVIP, on_delete=models.SET_NULL, blank=True, null=True, related_name="viviendas")
    direccion = models.CharField(max_length=255)
    metros_cuadrados = models.DecimalField(max_digits=10, decimal_places=2)
    precio = models.DecimalField(max_digits=15, decimal_places=2)
    estado = models.CharField(max_length=50, choices=[
        ('En construcción', 'En construcción'),
        ('Terminada', 'Terminada'),
        ('Vendida', 'Vendida')
    ])
    foto = models.FileField(upload_to='vivienda',null=True,blank=True)
    
    def __str__(self):
        return f"{self.direccion} - {self.proyecto.nombre}"

class Costo(models.Model):
    id = models.AutoField(primary_key=True)  # ID autoincremental
    vivienda = models.ForeignKey(Vivienda, on_delete=models.CASCADE, related_name="costos", blank=True, null=True)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name="costos", blank=True, null=True)
    descripcion = models.CharField(max_length=255)
    monto = models.DecimalField(max_digits=15, decimal_places=2)
    fecha = models.DateField()

    def __str__(self):
        return f"{self.descripcion} - {self.monto}"
