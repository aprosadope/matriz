# Programa para gestionar la reserva de asientos en una sala de cine

# Crear la matriz de 3 filas por 4 columnas inicializada en 0
# Cada asiento se representa con 0 (libre) o 1 (reservado)
asientos = [[0 for columna in range(4)] for fila in range(3)]

# Solicitar al usuario la fila y columna del asiento que desea reservar
fila = int(input("Ingrese la fila del asiento (0-2): "))
columna = int(input("Ingrese la columna del asiento (0-3): "))

# Validar que los índices estén dentro del rango permitido
if 0 <= fila < 3 and 0 <= columna < 4:
    # Verificar si el asiento está libre
    if asientos[fila][columna] == 0:
        asientos[fila][columna] = 1  # Reservar el asiento
        print(" Asiento reservado correctamente.")
    else:
        print(" Ese asiento ya está reservado.")
else:
    print(" Posición inválida. Recuerde que filas válidas son 0-2 y columnas válidas son 0-3.")

# Mostrar el estado actual de la sala
print("\nEstado de la sala de cine:")
for fila in asientos:          # Recorrer cada fila de la matriz
    for asiento in fila:        # Recorrer cada asiento dentro de la fila
        print(asiento, end=" ") # Imprimirlos valores en la misma línea
    print()                     # Salto de línea al terminar cada fila
