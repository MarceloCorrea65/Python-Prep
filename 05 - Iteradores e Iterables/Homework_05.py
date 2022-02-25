# Iteradores e iterables

# 1) A partir de una lista vacía, utilizar un ciclo while para cargar allí números negativos del -15 al -1

n = -15
numeros_1 = []
while(n<0):
    numeros_1.append(n)
    n +=1
print(numeros_1)

# 2) ¿Con un ciclo while sería posible recorrer la lista para imprimir sólo los números pares?

n = 0
while(n <16):
    if (numeros_1[n] % 2 == 0):
        print('El número',numeros_1[n],'es par')
        n +=1

# 2) ¿Con un ciclo while sería posible recorrer la lista para imprimir sólo los números pares?

n = 0
while(n<15):
    if (numeros_1[n]%2 == 0):
        print('El número',numeros_1[n],'es par')
    n +=1

# 3) Resolver el punto anterior sin utilizar un ciclo while

for n in numeros_1:
    if(n % 2 == 0):
        print('El número',n,'es par')

# 4) Utilizar el iterable para recorrer sólo los primeros 3 elementos

for n in numeros_1[:3]:
    print(n)

# 5) Utilizar la función **enumerate** para obtener dentro del iterable, tambien el índice al que corresponde el elemento

for n1, n2 in enumerate(numeros_1[:3]):
    print(n1,n2)

# 6) Dada la siguiente lista de números enteros entre 1 y 20, crear un ciclo donde se completen los valores faltantes: lista = [1,2,5,7,8,10,13,14,15,17,20]

lista = [1,2,5,7,8,10,13,14,15,17,20]
n = 1
while(n < 21):
    if(not(n in lista)):
        lista.insert(n-1,n)
    n += 1
print(lista)

# 7) La sucesión de Fibonacci es un listado de números que sigue la fórmula:
# n0 = 0
# n1 = 1
# ni = ni-1 + ni-2
# Crear una lista con los primeros treinta números de la sucesión.

fibo = [0,1]
n = 2
while(n < 30):
    fibo.append(fibo[n-1]+fibo[n-2])
    n += 1
print(fibo)

# 8) Realizar la suma de todos elementos de la lista del punto anterior

print(sum(fibo))

# 9 La proporción aurea se expresa con una proporción matemática que nace el número irracional Phi= 1,618… que los griegos llamaron número áureo. El cuál se puede aproximar con la sucesión de Fibonacci. Con la lista del ejercicio anterior, imprimir el cociente de los últimos 5 pares de dos números contiguos:
# Donde i es la cantidad total de elementos
# ni-1 / ni
# ni-2 / ni-1
# ni-3 / ni-2
# ni-4 / ni-3
# ni-5 / ni-4

mayor = 29
menor = mayor - 5
serie = []
while(menor < mayor):
    serie.append(fibo[menor]/fibo[menor+1])
    menor += 1
print(serie)

# 10) A partir de la variable cadena ya dada, mostrar en qué posiciones aparece la letra "n"
# cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'

cadena = 'Hola Mundo. Esto es una práctica del lenguaje de programación Python'
n = []
for i, c in enumerate(cadena):
    if (c == 'n'):
        n.append(i)
print(n)

# 11) Crear un diccionario e imprimir sus claves utilizando un iterador

diccio = {'Nombres':['José','Juam'],'Apellidos':['Perez','Ortega'],'Matrícula':[123,456]}
for n in diccio:
    print(n)

# 12) Convertir en una lista la variable "cadena" del punto 10 y luego recorrerla con un iterador 

cadena = 'Hola Mundo. Esto es una práctica del lenguaje de programación Python'
cadena_lista = []
for x in cadena:
    cadena_lista.append(x)
print(cadena_lista)

# 13) Crear dos listas y unirlas en una tupla utilizando la función zip

lista_1 = [1,2,3,4,5]
lista_2 = ['1','2','3','4','5']
lista_unida = zip(lista_1,lista_2)
print(type(lista_unida))
print(lista_1)
print(lista_2)
print(list(lista_unida))

# 14) A partir de la siguiente lista de números, crear una nueva sólo si el número es divisible por 7
# lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]

lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]
lista_nueva = [n for n in lis if(n % 7 == 0)]
print(lista_nueva)

# 15) A partir de la lista de a continuación, contar la cantidad total de elementos que contiene, teniendo en cuenta que un elemento de la lista podría ser otra lista:
# lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]

lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]
cant = 0
for n in lis:
    if(type(n) == list):
        cant += len(n)
    else:
        cant += 1
print('La cantidad de elementos es:',cant)

# 16) Tomar la lista del punto anterior y convertir cada elemento en una lista si no lo es

lis_nueva = []
for n, p in enumerate(lis):
    if (type(p) != list):
        lis_nueva.insert([p])
    else:
        lis_nueva.insert(n,p)
print(lis_nueva)