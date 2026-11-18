import time
import random


def generar_intervalos(cantidad):
    elementos = [
        max(1, cantidad // 4),
        max(1, cantidad // 2),
        cantidad
    ]
    return sorted(set(elementos))


def generar_numeros(cantidad):
    inicio = time.perf_counter()
    datos = [random.randint(0, 1_000_000_000) for _ in range(cantidad)]
    fin = time.perf_counter()
    tiempo = fin - inicio
    return datos, tiempo


def sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]


cantidad = int(input("cantidad de elementos:"))
datos, tiempo = generar_numeros(cantidad)
print("Iniciar generacion.")
print(f"Tiempo de ejecucion: {tiempo:.4f}")
print("Fin de generacion")

ini = time.perf_counter()
print(datos)
fin = time.perf_counter()
dif = fin - ini

sort(datos)
print(datos)
print(f"Tiempo de ejecucion: {tiempo:.4f}")
print(f"Duracion de impresion {dif:.4f}")