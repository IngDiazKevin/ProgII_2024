from random import randrange

#--1) Mostrar el tablero
#Crear una funcion que permita mostrar el tablero
#Esta funcion acepta un parametro inicial que son 
#las ubicaciones del tablero
def MostrarTablero(tablero):
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   '+tablero[0][0]+'   |   '+tablero[0][1]+'   |   '+tablero[0][2]+'   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   '+tablero[1][0]+'   |   '+tablero[1][1]+'   |   '+tablero[1][2]+'   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   '+tablero[2][0]+'   |   '+tablero[2][1]+'   |   '+tablero[2][2]+'   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')

#MostrarTablero(tablero)

#--2) Para ingresar movimientos
#Esta funcion acepta el estado actual del tablero y PREGUNTA al usuario acerca de su movimiento
#Verifica la entrada y actualiza el tablero

def IngresarMoviento(tablero):
    while True:
        movimiento = int(input('Ingresa un numero entre 1 a 9: '))
        
        if movimiento<1 or movimiento>9:
            print('Por favor, ingresa un num entre 1 a 9')
            continue
        
        #En el tablero los num 1 al 9 son STR no INT
        #Entonces hago la conversion
        #Ademas pregunto si se encuentra en la fila 1,2 o 3
        elif str(movimiento) not in tablero[0] and str(movimiento) not in tablero[1] and str(movimiento) not in tablero[2]:
            print('El cuadro ya esta ocupado, seleciona otro')
            continue
        
        elif movimiento == 1:
            tablero[0][0] = 'O'
        elif movimiento == 2:
            tablero[0][1] = 'O'
        elif movimiento == 3:
            tablero[0][2] = 'O'
        
        elif movimiento == 4:
            tablero[1][0] = 'O'
        elif movimiento == 5:
            tablero[1][1] = 'O'
        elif movimiento == 6:
            tablero[1][2] = 'O'
            
        elif movimiento == 7:
            tablero[2][0] = 'O'
        elif movimiento == 8:
            tablero[2][1] = 'O'
        elif movimiento == 9:
            tablero[2][2] = 'O'
        break
            

            
#---3) 
#Esta funcion examina el tablero y contruye una lista con todos
#los cuadros vacios
#La lita esta compuesta por una tupla, cada tupla es un par de num
#que indican fila y columna

def CrearListaConEspaciosVacios(tablero):
    espacios_free = []
    
    for fila in range(0,3):
        for columna in range(0,3):
            if tablero[fila][columna] == 'X' or tablero[fila][columna] == 'O':
                pass
            else:
               
    
               espacios_free.append(([fila,columna]))
    print(espacios_free)
    return espacios_free
        

#---4
#Funcion para verificar la victoria

def VerificarVictoria(tablero, signo):
    if signo == 'O':
        print('Verificar si TU ganaste')
    else:
        print('Verificar si la PC ganó')
        
    for i in range(3):
        if tablero[i][0] == signo and tablero[i][1] == signo and tablero [i][2] == signo:
            return True
        if tablero[0][i] == signo and tablero[1][i] == signo and tablero [2][i] == signo:
            return True
        
    if tablero [0][0] == signo and tablero [1][1] == signo and tablero[2][2] == signo:
        return True
    if tablero [0][2] == signo and tablero[1][1] == signo and tablero[2][0] == signo:
        return True
    
    return False

#--5
#Funcion para el movimiento de la maquina

def MovimientoMaquina(tablero):
    while True:
        fila = randrange(3)
        columna = randrange(3)
        
        print('num ale',fila, columna)
        
        if (fila, columna) not in CrearListaConEspaciosVacios(tablero):
            #tablero[fila, columna] = 'X'
            continue
        else:
            tablero[fila][columna] = 'X'
            #break
            return
            #continue

#Codigo principal del juego
#Dibujar el tablero 
tablero = [['1','2','3'],['4','X','6'],['7','8','9']]
humano = 'O' 
computador = 'X'
numero_movimientos = 1

print('---- BIENVENIDO AL JUEGO ----')
print('')
print('')
print('Estado actual del tablero')
MostrarTablero(tablero)
print('')

while numero_movimientos < 9:
    IngresarMoviento(tablero)
    numero_movimientos = numero_movimientos + 1
    MostrarTablero(tablero)
    
    if VerificarVictoria(tablero, humano):
        print('GANASTE!')
        break
    else:
        print('Espacios vacios del tablero')
        CrearListaConEspaciosVacios(tablero)
      
    print('')    
    print('AHORA ES EL TURNO DE LA PC')
    MovimientoMaquina(tablero)
    numero_movimientos = numero_movimientos + 1
    MostrarTablero(tablero)
    print('')
    
    if VerificarVictoria(tablero, computador):
        print('LA PC HA GANADO! perdiste')
        break
    else:
        print('Espacios vacios del tablero')
        CrearListaConEspaciosVacios(tablero)
        MostrarTablero(tablero)
    
else:
    print('EMPATE')
    
print('gracias por jugar') 

        
    
    
    


#MostrarTablero(tablero)
#IngresarMoviento(tablero)
#MostrarTablero(tablero)
#CrearListaConEspaciosVacios(tablero)
