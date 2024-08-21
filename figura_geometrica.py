from abc import ABC, abstractclassmethod   #ABC (Abstract base class)


class FiguraGeometrica(ABC):   #Todas las clases abastractas necesitan nacer de ABC
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    @abstractclassmethod
    def area(self):
        pass
    
    
#ObjetoErroneo = FiguraGeometrica();  #Salta error porque no se puede crear objetos de
                                     #Clases abstratcas


    