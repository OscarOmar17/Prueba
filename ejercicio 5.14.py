"""
Ejercicio 5.14 Escriba un programa que lea números enteros del teclado. El programa debe leer los números
hasta que el usuario digite 0 (cero). Al final de la ejecución, exhiba la cantidad de números digitados, así
como la suma y la media aritmética.
"""

s = 0
cantidad_de_numeros = []
while True:
    numeros = int(input("Digite un número  presione 0 para salir: "))
    if numeros == 0:
        break
    else:
        s = s + numeros
        cantidad_de_numeros.append(s)
print("La suma de todos los números digitados es %d, el promedio de todos los números es %5.2f y la cantidad de números digitados es %d" %(s, s/len(cantidad_de_numeros), len(cantidad_de_numeros) ))
