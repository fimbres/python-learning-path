from Menu import Menu
from Productos import Productos
from Menu import Menu

class Golosinas(Menu,Productos):
    def __init__(self):
        self.public()

    def Metodo(self):
        self.public()

golosinas = Golosinas()
golosinas.Metodo()
golosinas.get_Producto()
print(golosinas.value)