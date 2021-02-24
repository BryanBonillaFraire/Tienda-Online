from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Cliente(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    price = models.FloatField()
    imagen = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.nombre

    @property
    def imageURL(self):
        try:
            url = self.imagen.url
        except:
            url = ""
        return url
    

class Envio(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    date_orderd = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        objetosenvio = self.objetosenvio_set.all()
        total = sum([item.get_total for item in objetosenvio])
        return total

    @property
    def get_cart_items(self):
        objetosenvio = self.objetosenvio_set.all()
        total = sum([item.cantidad for item in objetosenvio])
        return total
    

class ObjetosEnvio(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    envio = models.ForeignKey(Envio, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField(default=0, null=True, blank=True)
    fecha_agregado = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.producto.price * self.cantidad
        return total

class Domicilio(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    envio = models.ForeignKey(Envio, on_delete=models.SET_NULL, null=True)
    domicilio = models.CharField(max_length=200, null=True)
    ciudad = models.CharField(max_length=200, null=True)
    estado = models.CharField(max_length=200, null=True)
    cp = models.CharField(max_length=200, null=True)
    fecha_agregada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.domicilio