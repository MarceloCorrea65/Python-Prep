# Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

variable_01 = 12
print(variable_01)

# 2) Imprimir el tipo de dato de la constante 8.5

print(type(8.5))

# 3) Imprimir el tipo de dato de la variable creada en el punto 1

type(variable_01)

# 4) Crear una variable que contenga tu nombre

mi_primer_nombre = 'Marcelo'
mi_segundo_nombre = 'Horacio'
mi_apellido = 'Correa'
mi_nombre_completo = mi_primer_nombre + ' ' + mi_segundo_nombre + ' ' + mi_apellido
print(mi_nombre_completo)

# 5) Crear una variable que contenga un número complejo

var_compleja = 3 + 4j

# 6) Mostrar el tipo de dato de la variable crada en el punto 5

print(type(var_compleja))

# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

import math
print(round((math.pi), 4))

# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

var_TRUE = 'True'
var_True = True

# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9

print(type(var_TRUE))
print(type(var_True))

# 10) Asignar a una variable, la suma de un número entero y otro decimal

var_suma = 12 + 5.8
print(var_suma)

# 11) Realizar una operación de suma de números complejos

print(2+2j + 3-3j)

# 12) Realizar una operación de suma de un número real y otro complejo

print(2+2j + 3)

# 13) Realizar una operación de multiplicación

print(12.3 * 2.5)

# 14) Mostrar el resultado de elevar 2 a la octava potencia

print(2**8)

# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

print(27/4)

# 16) De la división anterior solamente mostrar la parte entera

print(27//4)

# 17) De la división de 27 entre 4 mostrar solamente el resto

print(27%4)

# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

print(6*4+3)

# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

var_a = 'primero'
var_b = 'segundo'
print(var_a + ' ' + var_b)

# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

print(2 == '2')

# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

print(str(2) == '2')
print(2 == int('2'))

# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

print(a = float('3,8'))
# usa coma y no punto para los decimales

# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido

var_3 = 3
var_3 -=2
print(var_3)

# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

print(1<<2)
# 0001(1) << 0100(4)

# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

print(2 + 2)
print(type(2 + 2))
print('2' + '2')
print(type('2' + '2'))
print(2 + '2')

# 26) Realizar una operación válida entre valores de tipo entero y string

var_num = 2
var_str = 'Boeing '
print(var_num * var_str + '- se repite ' + str(var_num) + ' veces')
