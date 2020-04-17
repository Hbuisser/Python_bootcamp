import sys

def operations(one, two):
    a = float(one)
    b = float(two)
    if a or b == 0:
        print("")
    add = a + b
    sous = a - b
    mul = a * b
    div = a / b
    mod = a % b
    print("Sum:       ", int(add))
    print("Difference:", int(sous))
    print("Product:   ", int(mul))
    print("Quotient:  ", div)
    print("Remainder: ", int(mod))

operations(sys.argv[1], sys.argv[2])