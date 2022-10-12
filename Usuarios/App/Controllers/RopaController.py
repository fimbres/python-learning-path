from django.shortcuts import render
from App.Models.ropa_model import Ropa_models

class RopaController:
    def index(request):
        ropa_list = Ropa_models.Ropa_list()
        context = {'ropa_list':ropa_list}
        return render(request, 'views/Ropa/Ropa.html', context)
    def details(request,prendaid):
        objects = Ropa_models.get_Ropa(prendaid)
        context = {'prenda':objects[0],'categoria':objects[1]}
        return render(request, 'views/Ropa/Ropa.html', context)