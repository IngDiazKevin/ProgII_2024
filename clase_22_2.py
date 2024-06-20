#Cuando se tiene una clase con varios parametros
#uno necesario (nombre)
#otro por defecto  (edad)
class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__edad = 18
        
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre
        
    def get_edad(self):
        return self.__edad
    def set_edad(self, edad):
        self.__edad = edad
        
persona1 = Persona('ALex')
print(persona1.get_nombre())
print(persona1.get_edad())

persona1.set_edad(41)
print(persona1.get_edad())