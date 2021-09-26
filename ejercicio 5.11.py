"""
Ejercicio: Escriba un programa para cucular la media aritmetica de 5 números
donde el usuario deba escribir cuales son esos 5 números
"""
# Este programa calcula la media aritmetica de 5 números
n = ["primer", "segundo", "tercero", "cuarto", "quinto"]
contador = 1
acumulador = 0
while contador <= 5:
    numeros = int(input("Escriba el %s  número: " % n[contador-1]))
    acumulador = acumulador + numeros
    contador +=1
print("La media aritmetica es %5.2f :" % (acumulador/5))
