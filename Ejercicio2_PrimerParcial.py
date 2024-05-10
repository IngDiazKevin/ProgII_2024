
bloques = int(input("Ingresa el número de bloques: "))

altura  = 0
bloques_usados = 0

niveles = 1

while bloques_usados < bloques:
    bloques_usados += niveles
    if bloques_usados > bloques:
        break
    else:
        altura += 1
        niveles += 1

print("La altura de la pirámide:", altura)