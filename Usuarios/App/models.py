from django.db import models

class Categorias(models.Model):
    CategoriaID = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Descripcion = models.CharField(max_length=50)
    Estado = models.BooleanField(True)

class Ropa(models.Model):
    Ropa_ID = models.AutoField(primary_key=True)
    Imagen = models.ImageField(null=True,upload_to='images/H1F.png')
    Nombre = models.CharField(max_length=50)
    Descrpcion = models.CharField(max_length=50)
    TallaS = models.IntegerField(default=6)
    TallaM = models.IntegerField(default=9)
    Costo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=False)
    CategoriaID = models.ForeignKey(Categorias, blank=True, null=True, on_delete=models.CASCADE)
    Estado = models.BooleanField(True)
