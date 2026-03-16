from django.contrib import admin
from .models import Comercio, Categoria, Producto

admin.site.register(Comercio)
admin.site.register(Categoria)
admin.site.register(Producto)