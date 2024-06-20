#Herencia
#Se tiene una clase padre->Persona con un Atribu(nombre,edad)
#Ademas se tiene una clase hija-> Empleado con ATribu(sueldo)
#La clase hija nace de la clase padre
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def __str__(self): #AUTOMATICO
        return "Nombre " + self.nombre + ", edad " + str(self.edad)
        
class Empleado(Persona):    #Una clase hija que nace de "Persona"
    def __init__(self, nombre, edad,sueldo):
        super().__init__(nombre,edad)
        self.sueldo = sueldo
    
    def __str__(self): #Sobreescritura
        return super().__str__() + ", sueldo "+ str(self.sueldo)

#Objeto de la clase padre
persona = Persona("Juan", 28)
print(persona)

empleado1 = Empleado("Maria", 29, 400)
print(empleado1)
        
#Verificar si apartir de la clase hija se puede
#acceder a argumento de la clase padre

empleado1.nombre = 'Esther'
empleado1.edad = 12

print(empleado1)