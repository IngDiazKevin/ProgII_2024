#Crear clases
class Persona: #Creando
    def __init__(self, nombre, edad):
        self.nombre = nombre  #self.atributo = argumento
        self.edad = edad 

#Modificando valores de la clase NO ES LO CORRECTO  
Persona.nombre = 'Alex'
Persona.edad = 23
print(Persona.nombre)
print(Persona.edad)

persona1 = Persona("Juan", 28)
print(persona1.nombre)
print(persona1.edad)
print(id(persona1))

persona2 = Persona("Maria", 18)
print(persona2.nombre)
print(persona2.edad)
print(id(persona2))


