salario = float(input("Ingresa tu salario: "))

if salario > 125000:
    aumento1 = salario + (salario * 0.1)
    print("Tu salario con el aumento es %5.2f" %aumento1)
else:
    aumento2 = salario + (salario * 0.15)
    print("Tu salario con el aumento es %6.2f" %aumento2)
