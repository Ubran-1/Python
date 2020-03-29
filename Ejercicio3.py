lista = []
cantidad=int (input("Cuantos numeros desea ingresar: "))
mayor=0
i=1

while(cantidad > 0):
    numero = int(input("Numero #" + str(i) + ":  "))
    lista.append(numero)
    i = i + 1
    cantidad = cantidad - 1


mayor = max(lista)

print("Lista: ", lista)
print("Mayor: ", mayor)
