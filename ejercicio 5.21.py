"""
Ejercicio 5.21 Reescriba el programa de la lista 5.14 de tal modo que continúe ejecutándolo hasta que el valor
digitado sea 0. Utilice repeticiones anidadas.
"""

cantidad = int(input("Digite el valor de la cantidad: "))
limite = 50
valor = cantidad
billetes_de_50 = 0
while limite <= valor:
    valor -= limite
    billetes_de_50 += 1
    billetes_de_20 = 0
    while valor >= 20:
        valor -= 20
        billetes_de_20 += 1
        billetes_de_10 = 0
        while valor >= 10:
            valor -= 10
            billetes_de_10 += 1
            billetes_de_5 = 0
            while valor >= 5:
                valor -= 5
                billetes_de_5 += 1
print( billetes_de_50, billetes_de_20)
