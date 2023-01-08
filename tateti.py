# FUNCIÓN QUE ACTUALIZA LISTA
def actualizaLista(lista):
    listaCasilleros = [casilleroA1, casilleroA2, casilleroA3, casilleroB1, casilleroB2, casilleroB3, casilleroC1, casilleroC2, casilleroC3]
    return listaCasilleros

# FUNCIÓN QUE PASA LISTA A CADENA
def listaCadena(lista):
    cadenaBase3 = ""
    for str in listaCasilleros:
        cadenaBase3 = cadenaBase3 + str
    return cadenaBase3

# FUNCIÓN QUE PASA DE BASE 3 A DECIMAL 
def conversorBase3Base10(cadenaBase3):
    numBase10 = 0 
    auxiliar = 0 
    exponente = len(cadenaBase3)-1 
    for str in cadenaBase3:
        auxiliar = int(str)
        numBase10 = numBase10 + auxiliar * (3 ** exponente)
        exponente = exponente - 1
    return numBase10
""""""""""""""""
from tkinter import *
from tkinter import ttk

def colocarXA1():
    ttk.Button(frm, text="X").grid(column=1, row=0)

def colocarXA2():
    ttk.Button(frm, text="X").grid(column=2, row=0)

def colocarXA3():
    ttk.Button(frm, text="X").grid(column=3, row=0)

def colocarXB1():
    ttk.Button(frm, text="X").grid(column=1, row=1)

def colocarXB2():
    ttk.Button(frm, text="X").grid(column=2, row=1)

def colocarXB3():
    ttk.Button(frm, text="X").grid(column=3, row=1)

def colocarXC1():
    ttk.Button(frm, text="X").grid(column=1, row=2)

def colocarXC2():
    ttk.Button(frm, text="X").grid(column=2, row=2)

def colocarXC3():
    ttk.Button(frm, text="X").grid(column=3, row=2)


root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()
ttk.Label(frm, text="TA-TE-TI INVENCIBLE").grid(column=0, row=0)
ttk.Button(frm, text="a1", command=(colocarXA1 and colocarXA2)).grid(column=1, row=0)
ttk.Button(frm, text="a2", command=colocarXA2).grid(column=2, row=0)
ttk.Button(frm, text="a3", command=colocarXA3).grid(column=3, row=0)
ttk.Button(frm, text="b1", command=colocarXB1).grid(column=1, row=1)
ttk.Button(frm, text="b2", command=colocarXB2).grid(column=2, row=1)
ttk.Button(frm, text="b3", command=colocarXB3).grid(column=3, row=1)
ttk.Button(frm, text="c1", command=colocarXC1).grid(column=1, row=2)
ttk.Button(frm, text="c2", command=colocarXC2).grid(column=2, row=2)
ttk.Button(frm, text="c3", command=colocarXC3).grid(column=3, row=2)
root.mainloop()


botonA1 = ttk.Button(frm, text="a1", command=root.destroy).grid(column=1, row=0)

casillasTablero = {"a1": None, "a2": None, "a3": None,
    "b1": 0, "b2": 0, "b3": 0,
    "c1": 0, "c2": 0, "c3": 0,}


print (casillasTablero)

casillasTablero["a1"] = 1

print (casillasTablero)


"""""""""

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<INICIO>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<
casilleroA1 = "0"
casilleroA2 = "0"
casilleroA3 = "0"
casilleroB1 = "0"
casilleroB2 = "0"
casilleroB3 = "0"
casilleroC1 = "0"
casilleroC2 = "0"
casilleroC3 = "0"

listaCasilleros = [casilleroA1, casilleroA2, casilleroA3, casilleroB1, casilleroB2, casilleroB3, casilleroC1, casilleroC2, casilleroC3]

print("inicio                   ", listaCasilleros)
#print (listaCadena(listaCasilleros))
cadenaBase3 = listaCadena(listaCasilleros)
#print (conversorBase3Base10(cadenaBase3))

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# PASAR LAS CADENAS A TUPLAS PARA QUE NO PUEDAN SER MOFICADAS LUEGO DE JUGAR 
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<PRIMER MOVIMIENTO>>>>>>>>>>>>>>>>>>>>>>>>>>>
# AJENO
# MODIFICAR VARIABLE -----> VÍA INTERFAZ GRÁFICA
casilleroB2 = "1"
# ACTUALIZAR LISTA
listaCasilleros = actualizaLista(listaCasilleros)
print("primer movimiento ajeno  ", listaCasilleros)
#print (listaCadena(listaCasilleros))
cadenaBase3 = listaCadena(listaCasilleros)
#print (conversorBase3Base10(cadenaBase3))

# PROPIO
if conversorBase3Base10(cadenaBase3) == 81:
    casilleroC3 = "2"
else:
    casilleroB2 = "2"

listaCasilleros = actualizaLista(listaCasilleros)
print("primer movimiento propio ", listaCasilleros)
#print (listaCadena(listaCasilleros))
cadenaBase3 = listaCadena(listaCasilleros)
#print (conversorBase3Base10(cadenaBase3))


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<SEGUNDO MOVIMIENTO>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 

# PRIMERO EN EL CENTRO 
# AJENO
# MODIFICAR VARIABLE -----> VÍA INTERFAZ GRÁFICA
casilleroA1 = "1"
# ACTUALIZAR LISTA
listaCasilleros = actualizaLista(listaCasilleros)
print("segundo movimiento ajeno ", listaCasilleros)
#print (listaCadena(listaCasilleros))
cadenaBase3 = listaCadena(listaCasilleros)
#print (conversorBase3Base10(cadenaBase3))
tableroEnDecimales = conversorBase3Base10(cadenaBase3)
# PROPIO
match tableroEnDecimales:
    case tableroEnDecimales if tableroEnDecimales == 6644: casilleroA3 = "2"
    case tableroEnDecimales if tableroEnDecimales == 2270: casilleroC2 = "2"
    case tableroEnDecimales if tableroEnDecimales == 812: casilleroC1 = "2"
    case tableroEnDecimales if tableroEnDecimales == 326: casilleroB3 = "2"
    case tableroEnDecimales if tableroEnDecimales == 110: casilleroB1 = "2"
    case tableroEnDecimales if tableroEnDecimales == 92: casilleroA3 = "2"
    case tableroEnDecimales if tableroEnDecimales == 86: casilleroA2 = "2"                 

listaCasilleros = actualizaLista(listaCasilleros)
print("segundo movimiento propio", listaCasilleros)
#print (listaCadena(listaCasilleros))
cadenaBase3 = listaCadena(listaCasilleros)
#print (conversorBase3Base10(cadenaBase3))

# PRIMERO FUERA DEL CENTRO 
# MOVIMIENTOS OBLIGATORIOS 
# PROPIO
match tableroEnDecimales:
    case tableroEnDecimales if tableroEnDecimales == 8910: casilleroA3 = "2"
    case tableroEnDecimales if tableroEnDecimales == 7452: casilleroA2 = "2"
    case tableroEnDecimales if tableroEnDecimales == 6966: casilleroC1 = "2"
    case tableroEnDecimales if tableroEnDecimales == 6732: casilleroB1 = "2"
    case tableroEnDecimales if tableroEnDecimales == 3078: casilleroA1 = "2"
    case tableroEnDecimales if tableroEnDecimales == 918: casilleroC3 = "2"
    case tableroEnDecimales if tableroEnDecimales == 892: casilleroB3 = "2"      
    case tableroEnDecimales if tableroEnDecimales == 190: casilleroA3 = "2"
    case tableroEnDecimales if tableroEnDecimales == 174: casilleroC3 = "2"
    case tableroEnDecimales if tableroEnDecimales == 172: casilleroC2 = "2"
    case tableroEnDecimales if tableroEnDecimales == 166: casilleroC1 = "2"
    
listaCasilleros = actualizaLista(listaCasilleros)
print("segundo movimiento propio", listaCasilleros)
#print (listaCadena(listaCasilleros))
cadenaBase3 = listaCadena(listaCasilleros)
#print (conversorBase3Base10(cadenaBase3))

# BUENOS MOVIMIENTOS
match tableroEnDecimales:
    case tableroEnDecimales if tableroEnDecimales == 189: casilleroA3 = "2"
    case tableroEnDecimales if tableroEnDecimales == 165: casilleroA3 = "2"
    case tableroEnDecimales if tableroEnDecimales == 163: casilleroA3 = "2"
    case tableroEnDecimales if tableroEnDecimales == 405: casilleroA1 = "2"
    case tableroEnDecimales if tableroEnDecimales == 171: casilleroA1 = "2"
    case tableroEnDecimales if tableroEnDecimales == 891: casilleroA1 = "2"
    case tableroEnDecimales if tableroEnDecimales == 2349: casilleroA3 = "2"      
    case tableroEnDecimales if tableroEnDecimales == 6723: casilleroA3 = "2"

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<TERCER MOVIMIENTO >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<
# AJENO
# MODIFICAR VARIABLE -----> VÍA INTERFAZ GRÁFICA
casilleroA2 = "1"
listaCasilleros = actualizaLista(listaCasilleros)
print("tercer movimiento ajeno  ", listaCasilleros)

# PROPIO
# PARA GANAR
if casilleroA1 == "0" and casilleroA2 == "2" and casilleroA3 == "2": 
    casilleroA1 = "2"
elif casilleroA1 == "2" and casilleroA2 == "0" and casilleroA3 == "2": casilleroA2 = "2"
elif casilleroA1 == "2" and casilleroA2 == "2" and casilleroA3 == "0": casilleroA3 = "2"

elif casilleroB1 == "0" and casilleroB2 == "2" and casilleroB3 == "2": casilleroB1 = "2"
elif casilleroB1 == "2" and casilleroB2 == "0" and casilleroB3 == "2": casilleroB2 = "2"
elif casilleroB1 == "2" and casilleroB2 == "2" and casilleroB3 == "0": casilleroB3 = "2"

elif casilleroC1 == "0" and casilleroC2 == "2" and casilleroC3 == "2": casilleroC1 == "2"
elif casilleroC1 == "2" and casilleroC2 == "0" and casilleroC3 == "2": casilleroC2 == "2"
elif casilleroC1 == "2" and casilleroC2 == "2" and casilleroC3 == "0": casilleroC3 == "2"

elif casilleroA1 == "0" and casilleroB1 == "2" and casilleroC1 == "2": casilleroA1 = "2"
elif casilleroA1 == "2" and casilleroB1 == "0" and casilleroC1 == "2": casilleroB1 = "2"
elif casilleroA1 == "2" and casilleroB1 == "2" and casilleroC1 == "0": casilleroC1 = "2"

elif casilleroA2 == "0" and casilleroB2 == "2" and casilleroC2 == "2": casilleroA2 = "2"
elif casilleroA2 == "2" and casilleroB2 == "0" and casilleroC2 == "2": casilleroB2 = "2"
elif casilleroA2 == "2" and casilleroB2 == "2" and casilleroC2 == "0": casilleroC2 = "2"

elif casilleroA3 == "0" and casilleroB3 == "2" and casilleroC3 == "2": casilleroA3 = "2"
elif casilleroA3 == "2" and casilleroB3 == "0" and casilleroC3 == "2": casilleroB3 = "2"
elif casilleroA3 == "2" and casilleroB3 == "2" and casilleroC3 == "0": casilleroC3 = "2"

elif casilleroA1 == "0" and casilleroB2 == "2" and casilleroC3 == "2": casilleroA1 = "2"
elif casilleroA1 == "2" and casilleroB2 == "0" and casilleroC3 == "2": casilleroB2 = "2"
elif casilleroA1 == "2" and casilleroB2 == "2" and casilleroC3 == "0": casilleroC3 = "2"  

elif casilleroC1 == "0" and casilleroB2 == "2" and casilleroA3 == "2": casilleroC1 = "2"  
elif casilleroC1 == "2" and casilleroB2 == "0" and casilleroA3 == "2": casilleroB2 = "2"
elif casilleroC1 == "2" and casilleroB2 == "2" and casilleroA3 == "0": casilleroA3 = "2"

listaCasilleros = actualizaLista(listaCasilleros)
print("tercer movimiento propio ", listaCasilleros)

# MOVIMIENTO RESIDUAL  
"""""
contador = 0 
for casillero in listaCasilleros:
    if casillero == "0" and contador == 0:
        casilleroA1= "2"
        break
    elif casillero == "0" and contador == 1: 
        casilleroA2= "2"
        break
    elif casillero == "0" and contador == 2: 
        casilleroA3= "2" 
        break
    elif casillero == "0" and contador == 3: 
        casilleroB1= "2" 
        break
    elif casillero == "0" and contador == 4:
        casilleroB2= "2" 
        break
    else: contador = contador + 1  
"""

contadorDeDos = 0
for str in listaCasilleros:
    if str == "2":
        contadorDeDos = contadorDeDos + 1
print("contidad de movimientos propios: ", contadorDeDos)

if contadorDeDos < 3:
    if casilleroA1 == "0":
        casilleroA1 = "2"
    elif casilleroA2 == "0": casilleroA2 = "2"
    elif casilleroA3 == "0": casilleroA3 = "2"
    elif casilleroB1 == "0": casilleroB1 = "2"
    elif casilleroB2 == "0": casilleroB2 = "2"
    else: casilleroB3 = "2"


listaCasilleros = actualizaLista(listaCasilleros) #--------> PLASMAR EN LA INTERFAZ GRÁFICA

print ("movimiento residual      ", listaCasilleros) 

# I WON! 

if casilleroA1 == "2" and casilleroA2 == "2" and casilleroA3 == "2":
    print ("I WON!")
elif casilleroB1 == "2" and casilleroB2 == "2" and casilleroB3 == "2": print ("I WON!")
elif casilleroC1 == "2" and casilleroC2 == "2" and casilleroC3 == "2": print ("I WON!")
elif casilleroA1 == "2" and casilleroB1 == "2" and casilleroC1 == "2": print ("I WON!")
elif casilleroA2 == "2" and casilleroB2 == "2" and casilleroC2 == "2": print ("I WON!")
elif casilleroA3 == "2" and casilleroB3 == "2" and casilleroC3 == "2": print ("I WON!")
elif casilleroA1 == "2" and casilleroB2 == "2" and casilleroC3 == "2": print ("I WON!")
elif casilleroC1 == "2" and casilleroB2 == "2" and casilleroA3 == "2": print ("I WON!")  
else: print ("empatamos :(")