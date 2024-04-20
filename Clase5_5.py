#Uso del metodo keys() para iterar un diccionario
diccionario = {
                'gato' : 'cat',
                'perro': 'dog',   
                'caballo': 'horse'}

for i in diccionario.keys():
    print(i, '->' , diccionario[i])