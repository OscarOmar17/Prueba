a = int(input("Escribe el primer número: "))
b = int(input("Escribe el segundo número: "))
acumulador = 0
dividendo = a
divisor = b
multiplo = b
mames = a
veces = []
while a > 0:
    acumulador = a - b
    a -= b
    if acumulador >= 0:
        veces.append(acumulador)
resultado = len(veces)
print("El resultado de la divición entera de %d ÷ %d = %d "  % (dividendo, divisor, resultado ))
acumulador1 = 0
while divisor > 0:
    acumulador1 = resultado + acumulador1
    divisor -= 1
residuo = mames - acumulador1
print ("El residuo es %d " % (residuo))
