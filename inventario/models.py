from django.db import models

class Comercio(models.Model):
    TIPO_CHOICES = [
        ('RETAIL', 'Supermercado/Kiosco'),
        ('TEXTIL', 'Indumentaria/Ropa'),
    ]
    nombre = models.CharField(max_length=150)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    direccion = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.get_tipo_display()})"

class Categoria(models.Model):
    comercio = models.ForeignKey(Comercio, on_delete=models.CASCADE, related_name='categorias', null=True, blank=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} - {self.comercio.nombre}"

class Producto(models.Model):
    comercio = models.ForeignKey(Comercio, on_delete=models.CASCADE, related_name='productos', null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    
    # Campos específicos (pueden quedar vacíos según el rubro)
    codigo_barras = models.CharField(max_length=50, blank=True, null=True) # Más para el súper
    talle = models.CharField(max_length=10, blank=True, null=True)         # Para la de ropa
    color = models.CharField(max_length=50, blank=True, null=True)         # Para la de ropa

    def __str__(self):
        return f"{self.nombre} ({self.comercio.nombre})"