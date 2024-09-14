from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    stock = models.PositiveIntegerField(default=0)
    imagen = models.ImageField(upload_to='productos/')
    descripcion = models.TextField(blank=True, max_length=60)
    
    def __str__(self):
        return self.nombre # Representa el objeto como el nombre del producto