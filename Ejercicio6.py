def factorial(x,n):
 if(n>0):
  x=factorial(x,n-1)
  x=x*n
 else:
  x=1
 return x
n=int(input("Ingrese un numero: "))
x=1
x=factorial(x,n)


print("El factorial de ",n," es: ")
print (x)