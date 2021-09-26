valor = int(input("Digite el valor a pagar: "))
billetes = 0
actual = 50
apagar = valor
while True:
    if actual <= apagar:
        apagar -= actual
        billetes += 1
    else:
        print("%d billete(s) de %d " % (billetes, actual))
        if apagar == 0:
            break
        elif actual  == 50:
            actual = 20
        elif  actual == 20:
            actual = 10
        elif actual == 10:
            actual = 5
        elif actual == 5:
            actual = 1
        billetes = 0 
