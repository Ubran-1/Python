def sumaprimos():
    numero = 0
    cont = 0
    total = 0
    while cont < 30:
        numero = float(input("Ingrese el numero: "))
        cont = cont + 1
        if numero % 2 == 0:
            total = total + numero
        else:
            total = total
    print("La suma de los primos es: " + str(total))


sumaprimos()