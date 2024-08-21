#Metodos estaticos y de clase
class MiClase:
    
    
    
    @staticmethod
    def metodo_estatico():
        print('Hola soy el Met Estatico');
    #El parametro SELF est asociado con Objeto
    #Por ello los Met Estaticos no acceden a Objetos
    
    #Segundo manera de crear metodos estaticos
    @classmethod
    def metodo_clase(cls):
        print('Hola soy el Met de Clase')
        
    #El cls hace referencia a la clase
    #ASi como en los Met de instancia tenia el SELF
    #en estos se tiene el cls, de CLASE
    
MiClase.metodo_estatico()
MiClase.metodo_clase()
    