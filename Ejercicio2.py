lista = []
cantidad=int (input("Cuantos numeros desea ingresar: "))
i=1
total=1
while(cantidad > 0):
    numero = int(input("Numero #" + str(i) + ":  "))
    lista.append(numero)
    i = i + 1
    cantidad = cantidad - 1
    total = total * numero


print("Lista: ", lista)
print(total)