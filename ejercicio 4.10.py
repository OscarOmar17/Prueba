consumo = float(input("¿Cuántos consumo de luz hiciste en kWh ? "))

tipo = 0
while True:
    print("""
    ¿Cuál es el tipo de instalación tienes?

    [1] Residencial
    [2] Comercial
    [3] Industrial
    [4] Salir del menu
    """)
    tipo = int(input("Elige una opción: "))
    if tipo == 1:
        if consumo <= 500:
            print("Tu costo es de %5.2f euros " % 0.40)
        elif consumo > 500:
            print("Tu costo es de %5.2f euros " % 0.65)
    elif tipo == 2:
        if consumo <= 1000:
            print("Tu costo es de %5.2f euros " % 0.55)
        elif consumo > 1000:
            print("Tu costo es de %5.2f euros " % 0.60)
    elif tipo == 3:
        if consumo <= 5000:
            print("Tu costo es de %5.2f euros " % 0.55)
        elif consumo > 5000:
            print("Tu costo es de %5.2f euros " % 0.60)
    elif tipo == 4:
        break
    else:
        print("Puro pinche cartel de santa a la verga compa")
