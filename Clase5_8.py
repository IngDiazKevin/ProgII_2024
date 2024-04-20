#Uso del metodo keys() para iterar un diccionario
diccionario = {
                'gato' : 'cat',
                'perro': 'dog',   
                'caballo': 'horse'}

#Agregar elemebtos a un diccionario
diccionario.update({'oso': 'beard'})
diccionario.popitem()   #El ultimo elemento del diccionario

#Eliminar elemntos de un diccionario
del diccionario['caballo']

print('For sin ordenar')
for i in diccionario.keys():
    print(i, '->' , diccionario[i])
    
print('For ordenado utilizando sorted')
for i in sorted(diccionario.keys()):
    print(i, '->' , diccionario[i])