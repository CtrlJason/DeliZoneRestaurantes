from django.db import models

# Create your models here.


class DatosUsuarios(models.Model):
    nombre = models.CharField(max_length=20, null=False, blank=False)
    celular = models.IntegerField(null=True)
    correo = models.EmailField(null=False, blank=False)
    asunto = models.TextField(null=True, blank=True, max_length=200)
