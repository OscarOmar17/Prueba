a = int(input("Escribe el primer número de la multiplicación: "))
b = int(input("Escribe el segundo número de la multiplicación: "))
acumulador = 0
m = b
while b > 0:
    acumulador = a + acumulador
    b -= 1
print ("El resultado de %d x %d = %d " % (a,m,acumulador))
