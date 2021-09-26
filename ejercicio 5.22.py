"""
Ejercicio 5.22 Escriba un programa que exhiba una lista de opciones (menú): adición, sustracción, división,
multiplicación y salir. Imprima la tabla de la operación elegida. Repita la ejecución del programa hasta que la
opción salida sea elegida.
"""
tabla = 1
while True:
    opcion = int(input("""
    ¿Cuál tabla quieres?
    [1] Suma
    [2] Resta
    [3] Multiplicación
    [4] División
    [5] Salir
    """))
    if opcion == 1:
        while tabla <= 10:
            numero = 1
            limite = int(input("¿Hasta donde quieres la tabla?: "))
            while numero <= limite:
                print("%d + %d = %d " %(tabla, numero, tabla + numero ))
                numero += 1
            tabla += 1
            break


    elif opcion == 2:
        while tabla <= 10:
            numero = 1
            limite = int(input("¿Hasta donde quieres la tabla?: "))
            while numero <= limite:
                print("%d - %d = %d " %(tabla, numero, tabla - numero ))
                numero += 1
            tabla += 1
            break

    elif opcion == 3:
        while tabla <= 10:
            numero = 1
            limite = int(input("¿Hasta donde quieres la tabla?: "))
            while numero <= limite:
                print("%d x %d = %d " %(tabla, numero, tabla * numero ))
                numero += 1
            tabla += 1
            break


    elif opcion == 4:
        while tabla <= 10:
            numero = 1
            limite = int(input("¿Hasta donde quieres la tabla?: "))
            while numero <= limite:
                print("%d ÷ %d = %5.2f " %(tabla, numero, tabla / numero ))
                numero += 1
            tabla += 1
            break

    else:
        break
