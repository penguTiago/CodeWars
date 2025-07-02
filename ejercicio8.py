'''
Escribe una función que reciba tres números enteros positivos como parámetros, 
cada uno representando la longitud de un lado de un triángulo.

La función debe determinar si los tres lados pueden formar un triángulo válido. 
En caso afirmativo, debe retornar un string indicando qué tipo de triángulo es:
- "equilátero" si los tres lados son iguales,
- "isósceles" si solo dos lados son iguales,
- "escaleno" si todos los lados son diferentes.

Si los lados no forman un triángulo válido, la función debe retornar 
el string "no es un triángulo".

Por ejemplo:
- Si los lados son 3, 3 y 3 → debe retornar "equilátero"
- Si son 4, 3 y 4 → "isósceles"
- Si son 3, 4 y 5 → "escaleno"
- Si son 1, 2 y 3 → "no es un triángulo"

hint: Recuerda que para que tres lados formen un triángulo, la suma de las longitudes 
de cualquier par de lados debe ser mayor que el tercer lado.
'''

def tipo_triangulo(a, b, c):
    pass

print(tipo_triangulo(3,3,3))
print(tipo_triangulo(4,3,4))
print(tipo_triangulo(3,4,5))
print(tipo_triangulo(1,2,3))
