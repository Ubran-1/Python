def fibonacci():
    a = 0
    b = 1
    c = 0
    contador=0

    Secuencia= int(input("Introduzca la cantidad que quiere ver: "))

    while contador < Secuencia:
        a=b
        b=c
        c=a+b
        print(c)
        contador=contador+1


fibonacci()