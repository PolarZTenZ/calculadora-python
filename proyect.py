# Función para obtener un número válido
def obtener_numero():
    while True:
        try:
            numero = float(input("Ingresa un dígito: "))
            return numero
        except ValueError:
            print("¡Eso no es un número válido! Reintenta.")

# Función para obtener la operación válida
def obtener_operacion():
    while True:
        operacion = input("Elige una operación (+, -, *, /, %): ")
        if operacion in ["+", "-", "*", "/", "%"]:
            return operacion
        else:
            print("Operación no válida. Elige una de (+, -, *, /, %).")

# Pedir los números al usuario
num1 = obtener_numero()
num2 = obtener_numero()

# Pedir la operación
operacion = obtener_operacion()

# Realizar la operación
if operacion == "+":
    resultado = num1 + num2
elif operacion == "-":
    resultado = num1 - num2
elif operacion == "*":
    resultado = num1 * num2
elif operacion == "/":
    if num2 != 0:  # Evitar división por cero
        resultado = num1 / num2
    else:
        resultado = "Error: No se puede dividir por el valor cero"
elif operacion == "%":
    resultado = num1 % num2

# Mostrar el resultado
print("Rpta:", resultado)
