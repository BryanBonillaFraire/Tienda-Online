from django.contrib import admin
from .models import Cliente, Producto, Envio, ObjetosEnvio, Domicilio

admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Envio)
admin.site.register(ObjetosEnvio)
admin.site.register(Domicilio)
