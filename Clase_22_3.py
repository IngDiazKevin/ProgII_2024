#Metodo privado y parcialmente privados (protegidos)

class Persona:
    def __init__(self, nombre, ape_paterno, ape_materno):
        self.nombre = nombre # publico
        self._ape_paterno = ape_paterno # pp
        self.__ape_materno = ape_materno #privdo
        
    def __metodo_privado(self):
        print(self.nombre)
        print(self._ape_paterno)
        print(self.__ape_materno)
        
    def metodo_publico(self):
        return self.__metodo_privado()
        

persona1 = Persona("Juan", "Lopez", "Perez")
#persona1.__metodo_privado() salta un error porque es u privado
persona1.metodo_publico()
