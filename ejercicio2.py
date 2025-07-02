''''
Tienes una lista de listas con información de alumnos, esta lista puede contener 
distinta información y en distinto orden, pero siempre va a tener al menos el 
nombre y la nota final. Deberás definir una función notas_alumnos(lista), 
la cual recibe una lista de listas en el formato de mas abajo. La función deberá 
retornar una lista de tuplas, donde cada tupla contiene el nombre de un 
estudiante y su nota final. Por ejemplo, tu función deberá retornar:
 [('Alicia', 5.7), ('Marco', 4.8), etc]
'''
lista = [
[16848, 5.7, 'Alicia', 'Rojo'],
[19845, 4.8, 'Marco', 'Verde'],
[19515, 6.2, 'Federico', 'Azul']
]
def notas_alumnos(lista):
    pass

print(notas_alumnos(lista))