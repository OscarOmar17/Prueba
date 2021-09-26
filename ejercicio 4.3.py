a = float(input())
b = float(input())
c = float(input())

if a < b and a < c and b < c:
    print("EL numero mas pequeño es %5.2f" %a)
    print("EL numero mas grande es %5.2f" %c)
elif b < a and b < c and a < c:
    print("EL numero mas pequeño es %5.2f" %b)
    print("EL numero mas grande es %5.2f" %c)
elif (c < a and c < b and a < b):
    print("EL numero mas pequeño es %5.2f" %c)
    print("EL numero mas grande es %5.2f" %b)
else:
    print("EL numero mas pequeño es %5.2f" %c)
    print("EL numero mas grande es %5.2f" %a)
