#Encapsulamiento met set y get

class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
        
persona1 = Persona('Juan')
#print(persona1.__nombre) Salta un error porque nombre es privado
print(persona1.get_nombre())

persona2 = Persona('Karla')
print(persona2.get_nombre())
persona2.set_nombre('Andrea')
print(persona2.get_nombre())

