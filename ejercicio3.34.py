velocidad = float(input("Escriba su velocidad(en km/h): "))
if velocidad > 80:
    multa = 5*(velocidad - 80)
    print("Usted tiene una multa de %5.2f Euros " % multa)
else:
    print("Usted respeta los límites de velocidad")
