from django.contrib import admin
from django.utils.html import format_html
from .models import Categorias, Ropa

# Register your models here.
class CategoriasAdmin(admin.ModelAdmin):
    list_display = ("Nombre", "Descripcion", "Estado")
    search_fields = ('Nombre',)

class RopaAdmin(admin.ModelAdmin):
    list_display = ("Nombre", "Descrpcion", "Costo", "Estado")
    search_fields = ('Nombre',)
    def image_tag(self, obj):
        if obj.Imagen != None:
            return format_html(f'<img width="85" height="85" src="media/{obj.Imagen}" />')
        else:
            return format_html('<img width="85" height="85" src="static/images/Lodod2.png" />')

admin.site.register(Categorias,CategoriasAdmin)
admin.site.register(Ropa,RopaAdmin) 