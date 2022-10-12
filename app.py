class Animales:
    name = "Aves"

    def __init__(self,value):
        Animales.name = value
        Animales.group()

    def group():
        print(Animales.name)

    def __del__(self):
        print("Se ha eliminado")

animal = Animales("Arboles")
if hasattr(animal,"name"):
    joder = getattr(animal,"name","No existe")
    setattr(animal,"name","Pedro")
    joder = getattr(animal,"name","No existe")
    delattr(animal,"name")
print(joder)