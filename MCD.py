def MCD(primer_numero, segundo_numero):
    if primer_numero < segundo_numero:
        divisor = primer_numero
    else:
        divisor = segundo_numero

    while divisor > 0:
        if primer_numero % divisor == 0 and segundo_numero % divisor == 0:
            maximo_comun_divisor = divisor
            divisor = 0
        else:
            divisor -= 1
    return maximo_comun_divisor


primer_numero = int(input("Ingrese el primer número: "))
segundo_numero = int(input("Ingrese el segundo número: "))

print("El máximo común mayor es:", MCD(primer_numero, segundo_numero))