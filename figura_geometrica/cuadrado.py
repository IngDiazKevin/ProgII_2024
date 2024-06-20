from figura_geometrica import FiguraGeometrica
from color import Color

class Cuadrado(FiguraGeometrica,Color):
    def __init__(self, lado, color):
        #super.__init__(self, ancho) no se usa
        #En cambio como alternativa del SUPER en Herencia multiple
        #Se importa el init de manera directa
        FiguraGeometrica.__init__(self,lado,lado)
        Color.__init__(self, color)
        
    def area(self):
        return self.ancho* self.alto
    

    

