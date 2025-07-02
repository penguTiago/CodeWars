""""
👉 Reto: texto en negrita Escribe un validador de tablero de Sudoku de 9x9. 
El tablero se recibe como lista de listas de enteros. Debes verificar que:
    -cada fila contenga números del 1 al 9 sin repetir
    -cada columna contenga números del 1 al 9 sin repetir
    -cada subcuadro 3x3 contenga números del 1 al 9 sin repetir
Entrada: lista de listas 9x9 Salida: "Tablero válido" o "Tablero inválido"
"""





def validar_sudoku(tablero):
    # TODO: recorrer filas
    for fila in tablero:
        if not es_valida(  ):  # completar
            return "Tablero inválido"

    # TODO: recorrer columnas
    for col in range(9):
        columna = []
        for fila in range(9):
            # TODO: agregar el valor correcto a columna
            pass
        if not es_valida(  ):  # completar
            return "Tablero inválido"

    # TODO: recorrer subcuadros 3x3
    for box_row in range(  ):  # completar
        for box_col in range(  ):  # completar
            subcuadro = []
            for i in range(3):
                for j in range(3):
                    # TODO: agregar elemento correspondiente
                    pass
            if not es_valida(  ):  # completar
                return "Tablero inválido"

    return "Tablero válido"

def es_valida(grupo):
    # TODO: filtrar solo valores 1..9
    numeros = []
    # TODO: llenar numeros con los elementos válidos

    # TODO: condición de validez con set y all()
    return True  # reemplazar por condición real

# Tablero de prueba
tablero = [
    [5,3,4,6,7,8,9,1,2],
    [6,7,2,1,9,5,3,4,8],
    [1,9,8,3,4,2,5,6,7],
    [8,5,9,7,6,1,4,2,3],
    [4,2,6,8,5,3,7,9,1],
    [7,1,3,9,2,4,8,5,6],
    [9,6,1,5,3,7,2,8,4],
    [2,8,7,4,1,9,6,3,5],
    [3,4,5,2,8,6,1,7,9]
]

print(validar_sudoku(tablero))  # Tablero válido