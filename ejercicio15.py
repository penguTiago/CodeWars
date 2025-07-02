'''
Escribe un programa que simule una trivia interactiva.

El programa recibirá como parámetro una base de datos en forma de diccionario, 
donde cada elemento representa una pregunta con sus opciones y la respuesta correcta.

Tu función debe elegir al azar una de las preguntas disponibles, mostrar en consola:

- El enunciado de la pregunta
- Las opciones posibles (letra y texto)
- Pedirle al usuario que elija una opción (por ejemplo escribiendo "A", "B", etc.)
- Indicar si su respuesta fue correcta o incorrecta

Cada ejecución debe mostrar una única pregunta, elegida al azar.  
No es necesario eliminar preguntas ni evitar repeticiones.

Hint: en la librería `random`, existe una función llamada `randint()` que 
puede usarse para obtener un índice aleatorio de una lista. 
Por ejemplo, si tenés una lista `[1, 2, 3, 4]`, podrías obtener un índice entre 0 y 3.
'''

from random import randint
base_preguntas = [
    {
        "pregunta": "¿Qué tipo de dato representa números enteros en Python?",
        "opciones": {
            "A": "str",
            "B": "float",
            "C": "int",
            "D": "bool"
        },
        "respuesta": "C"
    },
    {
        "pregunta": "¿Cómo se imprime algo en pantalla en Python?",
        "opciones": {
            "A": "echo()",
            "B": "print()",
            "C": "say()",
            "D": "mostrar()"
        },
        "respuesta": "B"
    },
    {
        "pregunta": "¿Qué símbolo se usa para hacer comentarios en una sola línea?",
        "opciones": {
            "A": "//",
            "B": "/* */",
            "C": "#",
            "D": "--"
        },
        "respuesta": "C"
    },
    {
        "pregunta": "¿Cuál es la función para obtener la longitud de una lista?",
        "opciones": {
            "A": "count()",
            "B": "length()",
            "C": "size()",
            "D": "len()"
        },
        "respuesta": "D"
    },
    {
        "pregunta": "¿Qué palabra reservada se usa para definir una función?",
        "opciones": {
            "A": "function",
            "B": "define",
            "C": "def",
            "D": "func"
        },
        "respuesta": "C"
    }
]

def trivia(base_preguntas):
    pass



trivia(base_preguntas)