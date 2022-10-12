'''fichero = open("prueba.txt",'w')
print(fichero.write("Lopez"))
print(fichero.readline())'''

'''def mi_decorador(arg):
    def decorador(funcion):
        def nueva(a,b):
           value = funcion(a,b)
           print(f"{arg} {value}")
        return nueva
    return decorador

@mi_decorador("La suma es: ")
def suma(a,b):
    return a+b'''

def log(fichero, arg):
    def decorador(funcion):
        def nueva(a,b):
            with open(fichero,'a') as openedfile:
                value = funcion(a,b)
                openedfile.write(f"{arg} {value}\n")
        return nueva
    return decorador

@log('ficherosalida.log',"La suma es: ")
def suma(a,b):
    return a+b

def operaciones(op):
    def multi(a,b):
        return a * b
    def divi(a,b):
        return a // b
    def restar(a,b):
        return a - b
    def sumar(a,b):
        return a + b
    if op == "multi":
        return multi
    if op == "divi":
        return divi
    if op == "resta":
        return restar
    if op == "suma":
        return sumar

suma(4,5)
#funcion = operaciones("divi")
#print(funcion(10,2))