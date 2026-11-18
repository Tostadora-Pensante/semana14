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

def ordenamiento_insercion(lista):
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > actual:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual
    return lista

cantidad = int(input("Cantidad de elementos: "))
print("Iniciar generación...")
datos, tiempo_gen = generar_numeros(cantidad)
print(f"Tiempo de generación: {tiempo_gen:.4f} segundos")
print("Fin de generación")

print("\nLista original (primeros 20 elementos):")
print(datos[:20])

print("*13")
print("=Ordenamiento por insercion=")
ini = time.perf_counter()
datos_insercion = ordenamiento_insercion(datos.copy())
fin = time.perf_counter()
print(f"Tiempo de ordenamiento (inserción): {fin - ini:.4f} segundos")
print("Primeros 20 elementos ordenados:", datos_insercion[:20])

input("\nPresione cualquier tecla para continuar...")
