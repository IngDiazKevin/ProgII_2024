#Integrando funciones parametrizadas:

def suma(a,b,c):
  print(a, '+' , b, '+',c, ' = ' ,a+b+c)

print('Usando argumentos posicionales')
suma(4,5,6)

print('Usando argumentos de palabra clave')
suma(c = 6, a = 4, b = 5)

print('Combinando ambos')
#suma(3, a = 1, b = 2)
suma(4, c  =6, b = 5)

#Lo que no se puede hacer es pasar parametros que no exiten