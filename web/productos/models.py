from django.db import models

# Create your models here.

class Producto (models.Model):
    nombre = models.CharField(max_length=200)
    stock = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/imagenes/')

    def __str__(self):
        return self.nombre