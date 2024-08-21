#Relacionar Metodos con Variables
class MiClase:
    
    variable_clase = 'Hola soy Var de Clase'
    
    @staticmethod
    def metodo_estatico():
        print('Hola soy el Met Estatico');
        print(MiClase.variable_clase);
    
    #Segundo manera de crear metodos estaticos
    @classmethod
    def metodo_clase(cls):
        print('Hola soy el Met de Clase')
        print(cls.variable_clase)
        #el cls hace referencia a la clase 
        #no puede ser el SELF porque eso es para objetos
        

MiClase.metodo_estatico()
MiClase.metodo_clase()
    