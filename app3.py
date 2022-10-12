#Excepciones

try:
    78/0
    raise Exception("lol")
except Exception as e:
    print(f"se obtuvo la siguiente excepcion {e}")
else:
    print("Todo bien")
finally:
    print("Entro en finally")
