from Aves import Aves

class Pinguino(Aves):
    __nombre = "Ricky"
    @property
    def getVolar(self):
        return self.__nombre
    @getVolar.setter
    def setVolar(self, valor):
        self.__nombre=valor
    def volar(self):
        print("Si puedo volar")