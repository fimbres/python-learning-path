from Aves import Aves
from Pelicano import Pelicano
from Pinguino import Pinguino

def atributo(value):
    assert value > 0
    return value - 5

pp = Pelicano()
#print(pp.getVolar)
#pp.setVolar = "lol"
#print(pp.getVolar)
print(atributo(5))
assert isinstance(pp,Pinguino)