#Atributos de clase
"""
Son atributos que se asocian a una clase y no al objeto de la clase
tambien llamadas Var Estaticas
Y en cada objeto de la clase se replica su valor

"""

class MiClase: 
    #Variable de instancia (objeto)
    def __init__(self, var_instancia):
        self.var_instancia = var_instancia
    #Esta asociada a objeto 

    #Variable de clase
    var_clase = "Hola soy la variable de clase"
    #Esta esta asociada a la clase 
    

#Acceder a las variables de clase (NO ES NECEARIO CREAR UN OBJETO):
print(MiClase.var_clase);

#Para acceder a las variables de instancia SE TIENE QUE TENER UN OBJETO si o si
objeto1 = MiClase("Hola soy VAr de instancia del Obj 1")
print(objeto1.var_instancia);
    
    
#Sin embargo, es posible acceder de manera directa
MiClase.var_instancia = "Modificando valor de Var instancia"
print(MiClase.var_instancia);

print(objeto1.var_instancia);




    