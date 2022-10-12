from abc import ABCMeta
from abc import abstractclassmethod

class Aves(metaclass = ABCMeta):
#Interfaz informal
#    def volar(self):
#        pass
#
#    def nadar(self):
#        pass


#Interfaz formal
    @abstractclassmethod
    def volar(self):
        pass
    @abstractclassmethod
    def nadar(self):
        pass