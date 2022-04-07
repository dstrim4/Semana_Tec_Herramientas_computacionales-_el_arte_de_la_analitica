"""Ejemplos Clase"""
"""
cualquierNum = float(input("Inserta un numero: "))
algo = cualquierNum **2.0
print(cualquierNum, "al cuadrado es ", algo)

cateto_a = float(input("Inserta la longitud del primer cateto: ")) 
cateto_b = float(input("Inserta la longitud del segundo cateto "))

print("La longitud de la hipotenusa es: ", (cateto_a**2 + cateto_b**2) ** .5)

nom = input("¿Me puedes dar tu nombre por favor? ") 
ape = input("¿Me puedes dar tu apellido por favor? ") 
print("Gracias.") 
print("\nTu nombre es " + nom + " " + ape + ".")

print("+" + 10 * "-" + "+") 
print(("|" + " " * 10 + "|\n") * 5, end="") 
print("+" + 10 * "-" + "+")
"""
"""Lab1"""

print("Ingresa un valor flotante para a")
a = float(input())

print("Ingresa un valor flotante para b")
b = float(input())

print("La suma de a y b es igual a ", a + b)
print("La resta de a y b es igual a ", a - b)
print("La multiplicación de a y b es igual a ", a * b)
print("La division de a y b es igual a ", a / b)

"""Lab2"""

x = float(input("Dame x: "))
y = (1/(x + 1/(x + 1/(x+1/x))))

print("y =", y)

"""Lab3"""

hora = int(input("Hora de inicio (horas): "))
min = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

horaFin = (((hora * 60) + min) + dura) / 60
minFin = (((hora * 60) + min) + dura) % 60

tiempoFin = str(round(horaFin)) + ":" + str(minFin)
print(tiempoFin)
