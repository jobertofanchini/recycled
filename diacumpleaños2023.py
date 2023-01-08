while True: 
    try:
        dia = int(input ("Ingrese el número del día de su cumpleaños: "))
        mes = int(input ("Ingrese el número del mes de su cumpleaños: "))
        break
    except:
        print ("No ingresó los datos correctamente.")
    
diasMeses2023 = 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31

if dia > 31 or dia <= 0 or mes > 12 or mes <= 0:
    print ("Colocó una fecha inválida.")

elif (mes == 2 and dia > 29) or (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30:
    print ("Colocó una fecha inválida.")
   
else:
    print ("Su cumpleaños en el 2023 cae: ", end ="")
    
    cantidadDias = 0
    for i in diasMeses2023[0: mes-1]:
        cantidadDias += i

    cantidadDiasTotal = cantidadDias + dia
    
    match cantidadDiasTotal:
        case cantidadDiasTotal if cantidadDiasTotal % 7 == 1: print ("Domingo")
        case cantidadDiasTotal if cantidadDiasTotal % 7 == 2: print ("Lunes")
        case cantidadDiasTotal if cantidadDiasTotal % 7 == 3: print ("Martes")
        case cantidadDiasTotal if cantidadDiasTotal % 7 == 4: print ("Miércoles")
        case cantidadDiasTotal if cantidadDiasTotal % 7 == 5: print ("Jueves")
        case cantidadDiasTotal if cantidadDiasTotal % 7 == 6: print ("Viernes")
        case cantidadDiasTotal if cantidadDiasTotal % 7 == 0: print ("Sábado")