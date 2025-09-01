def calcular(a, b, operacion):
    if operacion == '+':
        return a + b
    elif operacion == '-':
        return a - b
    elif operacion == '*':
        return a * b
    elif operacion == '/':
        return a / b if b != 0 else "Error: división por cero"

a = float(input("Número 1: "))
b = float(input("Número 2: "))
op = input("Operación (+, -, *, /): ")
print("Resultado:", calcular(a, b, op))