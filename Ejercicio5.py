def numpares():
    numero= int(input("Cuantos numeros desea ingresar: "))
    primero = 0
    cont = 0
    suma = 0
    while cont < numero:
        primero = float(input("Ingrese el numero: "))
        cont = cont + 1
        if primero % 2 == 0:
            suma = suma + primero
        else:
            suma = suma
    print("La suma total de numeros pares es: " + str(suma))


numpares()