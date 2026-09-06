# Crear una matriz vacía de 5 filas por 5 columnas
matriz = []

# Usar bucles anidados para recorrer filas y columnas
for i in range(5):
    fila = []  # Lista temporal para cada fila
    for j in range(5):
        # Solicitar al usuario cada valor
        valor = int(input(f"Ingrese el valor para la posición ({i}, {j}): "))
        fila.append(valor)  # Almacenar en la fila
    matriz.append(fila)  # Agregar la fila complet5a a la matriz

# Mostrar la matriz organizada
print("\nMatriz ingresada:")
for fila in matriz:
    for valor in fila:
        print(valor, end=" ")
    print()  # Salto de línea al terminar cada fila
#fin