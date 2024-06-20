class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  #Metodo privado
        self.edad = edad
        
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre
        
persona1 = Persona("Juan") 
#print(persona1.__nombre)   genera un error
print(persona1.get_nombre())

persona1.set_nombre("Pedro")
print(persona1.get_nombre())

#Por cada argumento (nombre, edad, etc) se tiene un propio GET y SET
