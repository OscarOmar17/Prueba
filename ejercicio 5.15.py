"""
Ejercicio 5.15 Escriba un programa para controlar una pequeña máquina registradora. Usted debe solicitarle al
usuario que digite el código del producto y la cantidad comprada. Utilice la tabla de códigos que aparece
abajo para obtener el precio de cada producto:
"""
compras = []
while True:
    codigo = int(input("Elija el codigo del producto o presione 0 para salir: "))
    if codigo == 1:
        cantidad_de_productos = int(input("¿Cuántos productos son?: "))
        compras.append(0.50 * cantidad_de_productos)
    elif codigo == 2:
        cantidad_de_productos = int(input("¿Cuántos productos son?: "))
        compras.append(1.00 * cantidad_de_productos)
    elif codigo == 3:
        cantidad_de_productos = int(input("¿Cuántos productos son?: "))
        compras.append(4.00 * cantidad_de_productos)
    elif codigo == 5:
        cantidad_de_productos = int(input("¿Cuántos productos son?: "))
        compras.append(7.00 * cantidad_de_productos)
    elif codigo == 9:
        cantidad_de_productos = int(input("¿Cuántos productos son?: "))
        compras.append(8.00 * cantidad_de_productos)
    elif codigo == 0:
        print("El total de las compras es %5.2f " % sum(compras))
        break
    else:
        print("Código inválido")
