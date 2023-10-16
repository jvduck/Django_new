from argparse import MetavarTypeHelpFormatter
from django.db import models

# Create your models here.
class Categorias(models.Model):
    #correspodera a la clase categoria: 1 producto tendra 1 categoria, pero 1 categoria tendra muchos productos#
    #? Existira relacion 1 a M
    category_name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.category_name
class Meta:
    managed = True
    verbose_name = 'Categoria'
    verbose_name_plural = 'categorias'

class Productos(models.Model):
    """modelo para la creacion de objetos de producto"""
    nombre = models.CharField(max_length=30, null=False)
    precio = models.FloatField()
    stock = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='img_inventario', null=True, blank=True)
    categoria_fk = models.ForeignKey(Categorias, on_delete=models.CASCADE,default=1) #esta sera la FK que nos relaciona con la clase categoria
    
    def __str__(self):
        return self.nombre
    class Meta:
        managed = True
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
