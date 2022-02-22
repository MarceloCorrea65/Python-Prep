# Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

var_entero = 0
if (var_entero > 0):
    print('El numero es mayor a 0')
elif (var_entero < 0):
    print('El número es menor que 0')
else:
    print('El numero es igual a 0')

# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

var_1 = 'str'
var_2 = 9
if (type(var_1) == type(var_2)):
    print('Ĺas variables son del mismo tipo')
else:
    print('Las variables son de distinto tipo')

# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

for n in range(1, 21):
    if (n%2 == 0):
        print(str(n) + ' es par')
    else:
        print(str(n) + ' es impar')

# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

for n in range(0, 6):
    print(n**3)

# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

var_01 = 5
for n in range(1,var_01+1):
    print(n)

# 6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

var_02 = 8
fact = 1
if (var_02 > 0 and int(var_02) == var_02):
    n = 1
    while (n <= var_02):
        fact *=n
        n +=1
    print('El factorial de ' + str(var_02) + ' es: ' + str(fact))
    import math
    print(math.factorial(var_02))
else:
    print('No es posible calcular el factorial')

# 7) Crear un ciclo for dentro de un ciclo while

n1 = 1
while (n1 < 5):
    print('Pasada ' + str(n1))
    for n2 in range(0, 5):
        print(n2)
    n1 += 1

# 8) Crear un ciclo while dentro de un ciclo for

for n in range(0, 7):
    print('Pasada ' + str(n))
    n1 = 1
    while (n1 < 4):
        print(n1)
        n1 += 1

# 9) Imprimir los números primos existentes entre 1 y 30

primo = True
for n1 in range (1, 31):
    n3 = n1
    for n2 in range(2, n3):
        if( n3 % n2 == 0):
            primo = False
            # break
    if(primo):
        print('El número ' + str(n3) + ' es primo')
    primo = True

# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

primo = True
for n1 in range (1, 31):
    n3 = n1
    for n2 in range(2, n3):
        if( n3 % n2 == 0):
            primo = False
            break
    if(primo):
        print('El número ' + str(n3) + ' es primo')
    primo = True

# 12) Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?

primo = True
ciclos = 0
for n1 in range (1, 100):
    n3 = n1
    for n2 in range(2, n3-1):
        ciclos +=1
        if( n3 % n2 == 0):
            primo = False
            break
    if(primo):
        pass
        # print('El número ' + str(n3) + ' es primo')
    primo = True
print(ciclos)

primo = True
ciclos = 0
for n1 in range (1, 100):
    n3 = n1
    for n2 in range(2, n3-1):
        ciclos +=1
        if( n3 % n2 == 0):
            primo = False
            # break
    if(primo):
        pass
        # print('El número ' + str(n3) + ' es primo')
    primo = True
print(ciclos)

# 13) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

n = 100
while (n < 300):
    n +=1
    if(n % 12 != 0):
        continue
    print('El ńumero '+ str(n) + ' es divisible por 12')

# 14) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

n2 = 1
primo = True
seguir = True
while (seguir):
    for n1 in range(2, n2):
        if( n2 % n1 == 0):
            primo = False
            break
    if(primo):
        print('El número', n2 ,' es primo')
        print('¿Desea encontrar el siguiente número primo? (0 para terminar)')
        if (input() == '0'):
            seguir = False
            break
    primo = True
    n2 +=1

# 15) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

