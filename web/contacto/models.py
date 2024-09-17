from django.db import models

# Create your models here.

class DatosUsuarios(models.Model):
    nombre = models.CharField(max_length=20, null=False, blank=False)
    apellido = models.CharField(max_length=20, null=True)
    correo = models.EmailField(null=False, blank=False)
    descripcion = models.TextField(null=True, blank=True, max_length=200)