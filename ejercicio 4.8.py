numero1 = float(input("Ingresa un número: "))
numero2 = float(input("Ingresa un número: "))

opcion = 0
while True:
    print("""
    ¿Cuál operación quieres realizar?

    1) Sumar los dos números
    2) Restar los dos números
    3) Multiplicar los dos números
    4) Cambiar los números elegidos
    5) Apagar calculadora
    """)
    opcion = int(input("Elige una opción: "))
    if opcion == 1:
        print("La suma de los números %5.2f y %5.2f es %5.2f" %(numero1, numero2, numero1 + numero2))
    elif opcion == 2:
        print("La resta de los números %5.2f y %5.2f es %5.2f" %(numero1, numero2, numero1 - numero2))
    elif opcion == 3:
        print("La multiplicación de los números %5.2f y %5.2f es %5.2f" %(numero1, numero2, numero1 * numero2))
    elif opcion == 4:
        numero1 =float(input("Escribe un número: "))
        numero2 =float(input("Escribe un número: "))
        opcion = 0
        while True:
            print("""
            ¿Cuál operación quieres realizar?

            1) Sumar los dos números
            2) Restar los dos números
            3) Multiplicar los dos números
            4) Apagar calculadora
            """)
            opcion = int(input("Elige una opción: ") )
            if opcion == 1:
                print("La suma de los números %5.2f y %5.2f es %5.2f" % (numero1 , numero2, numero1 + numero2))
            elif opcion == 2:
                print("La resta de los números %5.2f y %5.2f es %5.2f" % ( numero1 , numero2, numero1 - numero2))
            elif opcion == 3:
                print("La multiplicación de los números %5.2f y %5.2f es %5.2f" % (numero1 , numero2, numero1 * numero2))
            elif opcion == 4:
                break
    elif opcion == 5:
        break
    else:
        print("No seas mamon")
