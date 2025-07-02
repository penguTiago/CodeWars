'''
El objetivo de este ejercicio, es que programes una función 
buscaminas que reciba como argumento a una matriz tablero 
y dos coordenadas x, y, y que entregue la cantidad de bombas 
que rodean a esa posición. Por ejemplo, si la el tablero dado 
es el representado en la tabla, y la posición viene dada por 
x=0 y y=0, tu función debe retornar el valor 2, ya que hay 
dos bombas rodeándola, en (0,1) y (1,0). Por otro lado, si 
el tablero es el mismo, y las coordenadas son x=1, y=1, tu 
función debe retornar 4, pues hay bombas rodeando la posición 
en (1,0), en (0,1), en (2,1) y en (2,2).

Hint: recuerda que el tablero puede ser de un tamaño arbitrario 
y que al escribir posiciones más grandes que ese tamaño o menores 
que 0, tu programa arrojará error.

Hint2: recuerda que en buscamina se verifican tambien las esquinas
'''

tablero = [
    [' ', 'X', ' ', 'X'],
    ['X', ' ', ' ', ' '],
    [' ', 'X', 'X', ' '],
    ['X', ' ', ' ', 'X']
    ]

def buscaminas(tablero, x, y):
    pass


print(buscaminas(tablero, 0, 0))
print(buscaminas(tablero, 1, 1))

