#Acceder a variables de instancia desde metodo
class MiClase:
    
    variable_clase = 'Hola soy Var de Clase'
    
    def __init__(self):
        self.variable_instancia = 'Hola soy Var de Inst'
    
    @staticmethod
    def metodo_estatico():
        print('Hola soy el Met Estatico');
        print(MiClase.variable_clase);
        #print(MiClase.variable_instancia);
        #Salta error xq para una VarInstancia se requiere
        #Un objeto, en este caso no tengo un objeto
        #DE hecho un Metodo estatico esta creado para no usar
        #objetos.
    
    #Segundo manera de crear metodos estaticos
    @classmethod
    def metodo_clase(cls):
        print('Hola soy el Met de Clase')
        print(cls.variable_clase)
        #print(cls.variable_instancia)
        #No se puede llamar a una var de instancia
        #dentro de un meto estatico
        
        
MiClase.metodo_estatico()
MiClase.metodo_clase()

objeto1 = MiClase()
print(objeto1.variable_instancia)
    
#Con metodos estaticos se puede acceder a un contexto estatico
#pero no se puede acceder a contexto dinamico (instancias/objt)

#Una alternativa es usar Var de instancia FUERA de la clase