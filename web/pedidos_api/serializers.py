from rest_framework import serializers

class ProductoCarritoSerializer(serializers.Serializer):
    producto_id = serializers.CharField()
    nombre = serializers.CharField()
    cantidad = serializers.IntegerField()
    precio_unidad = serializers.DecimalField(max_digits=10, decimal_places=2)
    imagen = serializers.CharField(required=False)

class CarritoSerializer(serializers.Serializer):
    productos = serializers.DictField(child=ProductoCarritoSerializer())
    cantidad_total = serializers.IntegerField()
    precio_total = serializers.DecimalField(max_digits=10, decimal_places=2)