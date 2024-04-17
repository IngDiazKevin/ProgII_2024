#Ejercicio propuesto:

#Escribe una función llamada contar_digitos_pares que tome un número entero
# positivo como entrada y devuelva el número de dígitos pares que contiene.
# Luego, pide al usuario que ingrese un número entero positivo y muestra el
# número de dígitos pares en ese número utilizando la función definida.

def contar_digitos_pares(numero):
    # Inicializamos un contador para los dígitos pares
    contador = 0

    # Iteramos sobre cada dígito en el número
    while numero > 0:
        # Obtenemos el último dígito del número
        digito = numero % 10
        # Si el dígito es par, incrementamos el contador
        if digito % 2 == 0:
            contador += 1
        # Eliminamos el último dígito del número
        numero = numero // 10

    return contador

# Pedimos al usuario que ingrese un número entero positivo
numero_usuario = int(input("Ingresa un número entero positivo: "))

# Llamamos a la función contar_digitos_pares y mostramos el resultado
cantidad_digitos_pares = contar_digitos_pares(numero_usuario)
print("El número tiene", cantidad_digitos_pares, "dígitos pares.")