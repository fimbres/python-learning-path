from django.db import models
from ..models import Ropa, Categorias

class Ropa_models():
    def Ropa_list():
        ropa = Ropa.objects.order_by('Nombre')
        return ropa
    def get_Ropa(idRopa):
        ropa = Ropa.objects.get(Ropa_ID=idRopa)
        for item in ropa:
            categoria = Categorias.objects.get(CategoriaID=item.CategoriaID.CategoriaID)
        return [ropa,categoria]