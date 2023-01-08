dictInicial = {}
totalAsado = 0
divisorPromedio = 0

ingresoParticipante = True
while ingresoParticipante:
    participante = input("Por favor ingrese el nombre del participante: ")
    try:
        montoPagado = float(input("Por favor ingrese el monto desembolsado: "))
    except Exception:
        print("El monto ingresado es inválido. Se lo tomará como 0.")
        montoPagado = 0
        dictInicial[participante] = montoPagado
        totalAsado += montoPagado
        divisorPromedio += 1
        montoPromedio = totalAsado / divisorPromedio
    while True:
        continuarIngreso = input("¿Desea agregrar otro participante? S/N: ").lower()
        if continuarIngreso == "n":
            ingresoParticipante = False
            break
        elif continuarIngreso == "s":
            break   

dictDeudores = {}
dictAcreedores = {}

for i, j in dictInicial.items():
    if j > montoPromedio:
        dictAcreedores[i] = j - montoPromedio
    elif j < montoPromedio:
        dictDeudores[i] = montoPromedio - j

if len(dictDeudores) == 0:
    print("Ningún participante debe nada.")

while len(dictDeudores) != 0:
    for i, j in dictDeudores.items():
        for i_, j_ in dictAcreedores.items():
            if j < j_:
                print(i, "le debe a", i_, "la suma de", j, "pesos.")
                dictAcreedores[i_] = j_ - j
                del (dictDeudores[i])
                break
            elif j > j_:
                print(i, "le debe a", i_, "la suma de", j_, "pesos.")
                dictDeudores[i] = j - j_
                del (dictAcreedores[i_])
                break
            else:
                print(i, "le debe a", i_, "la suma de", j, "pesos.")
                del (dictDeudores[i])
                del (dictAcreedores[i_])
                break
        break