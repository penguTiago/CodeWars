'''
Tienes una lista con información de países. Además, tienes una lista con 
el índice de belleza de los países, un país con un índice más alto se 
considera más bello que un país con el índice más bajo. Define la función 
paises_bellos(paises, belleza), que recibe como parámetro la lista paises 
y la lista belleza. La función deberá retornar una lista de tuplas, donde 
cada tupla contiene el nombre de un país y su índice de belleza. 
 La función deberá retornar: 
[('Francia', 0.81),
('Italia', 0.68),
('España', 0.62),
('Alemania', 0.57)]
'''
paises = [
[0, 'España', 'Madrid'],
[2, 'Alemania', 'Berlin'],
[1, 'Francia', 'Paris'],
[3, 'Italia', 'Roma']
]
belleza = [
[2, 0.57],
[1, 0.81],
[3, 0.68],
[0, 0.62]
]

def paises_bellos(paises, belleza):
    pass


print(paises_bellos(paises, belleza))