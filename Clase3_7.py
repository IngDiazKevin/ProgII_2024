#Observacion:
#Existe una circunstancia importante que se debe mencionar.
#Es posible tener una variable con el mismo nombre del parámetro de la función.
#El siguiente código muestra un ejemplo de esto:

def message(number):
    print("Ingresa un número:", number)

number = 1234
message(1)
print(number)

#Una situación como la anterior activa un mecanismo denominado sombreado:

#el parámetro x sombrea cualquier variable con el mismo nombre, pero...
#... solo dentro de la función que define el parámetro.
#El parámetro llamado number es una entidad completamente diferente de la variable llamada number.