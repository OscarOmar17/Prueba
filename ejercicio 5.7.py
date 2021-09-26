x = int(input("Escribe el inicio de tu tabla: "))
n = int(input("Escribe el fin de tu tabla: "))
m = int(input("Cual tabla quieres: "))
while x <= n:
    print("%d x %d = %d "%( m , x , m*x))
    x += 1
