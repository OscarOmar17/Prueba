valor_de_casa = float(input("¿Cuál es el valor de tu casa? "))
salario = float(input("¿Cuál es tu salario "))
años_a_pagar = float(input("¿En cuánto años vas a pagar? "))
meses = años_a_pagar * 12
cuota = valor_de_casa / meses
if cuota > (salario*0.3):
    print("Lo siento no podemos ofrecerle un prestamo pinche pobre")
else:
    print("¡Felicidades! usted puede obtener un prestamo de nuestro banco")
print(meses)
print(cuota)
print((salario*0.3))
