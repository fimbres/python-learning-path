from Generador import Generador

def funcion():
    return 4

def generador():
    yield 0
    yield 1
    yield 2
    yield 4

#print(funcion())
#print(next(generador()))
for i in Generador():
    print(i)

