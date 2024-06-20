class Aritmetica:
    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2
    
    def suma(self):
        return self.operando1 + self.operando2
    def resta(self):
        return self.operando1 - self.operando2
    def multiplicacion(self):
        return self.operando1 * self.operando2
    def division(self):
        return self.operando1 / self.operando2

resultado = Aritmetica(8, 4)
print("El resultado de la suma es:" , resultado.suma())
print(resultado.resta())
print(resultado.multiplicacion())
print(resultado.division())