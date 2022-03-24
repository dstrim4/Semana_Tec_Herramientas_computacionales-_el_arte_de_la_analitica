"""Pruebas clase"""
print("hola mundo...")
print("hola")
print("Bienvenido al curso - El arte de la análitica!")
print("Herramientas computacionales")
print("22")
print(7/11)
print(125./5.)
print(125/20)
print(125//20)
print(125%20)

"""Pytagoras"""
a = 3.0
b = 4.0
c = ((a**2) + (b**2))**0.5

""""Lab1 Manzanas cont de personas y total"""

juan = 3
maria = 5
adan = 6

print(str(juan) + ", " + str(maria) + ", " + str(adan))


totalManzanas = juan + maria + adan

print(totalManzanas)

""""Lab2 millas a kilometros y biseversa"""
millas = 7.38
km = 12.25
millasAkm = millas * 1.61
kmAmillas = km/1.61

print(millas, " millas son ", round(millasAkm, 2), " kilómetros ")
print(km, " kilómetros son ", round(kmAmillas, 2), " millas ")

""""Lab3 Horas segundos"""
print("Cuantas horas quieres pasar a segundos?")
horas =int(input())

seg = 3600 * horas
print("Los segundos de " + str(horas) + " horas es" + str(seg))
print("Adios KKS!!!!!")