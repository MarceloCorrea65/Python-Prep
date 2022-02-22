## Estructuras de Datos

# 1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla

ciudades = ['Buenos Aires','Montevideo','Brasilia','Bogotá','Caracas']
print(ciudades)

# 2) Imprimir por pantalla el segundo elemento de la lista

print(ciudades[1])

# 3) Imprimir por pantalla del segundo al cuarto elemento

print(ciudades[1:4])

# 4) Visualizar el tipo de dato de la lista

print(type(ciudades))

# 5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento

print(ciudades[2:])

# 6) Visualizar los primeros 4 elementos de la lista

print(ciudades[:4])

# 7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?

ciudades.append('Buenos Aires')
ciudades.append('Florianópolis')
print(ciudades)

# 8) Agregar otra ciudad, pero en la cuarta posición

ciudades.insert(3,'Lima')
print(ciudades)

# 9) Concatenar otra lista a la ya creada

paises = ['Argentina','Brasil','Perú']
ciudades.extend(paises)
print(ciudades)

# 10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?

print(ciudades.index('Buenos Aires'))

# 11) ¿Qué pasa si se busca un elemento que no existe?

print(ciudades.index('lima'))

# 12) Eliminar un elemento de la lista

ciudades.remove('Argetnina')

# 13) ¿Qué pasa si el elemento a eliminar no existe?

ciudades.remove('Uruguay')

# 14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo

ultimo = ciudades.pop()
print(ultimo)

# 15) Mostrar la lista multiplicada por 4

print(ciudades*4)

# 16) Crear una tupla que contenga los números enteros del 1 al 20

numeros = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
print(numeros)

# 17) Imprimir desde el índice 10 al 15 de la tupla

print(numeros[10:16])

# 18) Evaluar si los números 20 y 30 están dentro de la tupla

print(20 in numeros)
30 in numeros

# 19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.

mensaje = ''
if not('Paris' in ciudades) :
    mensaje = 'no existía'
    ciudades.append('Paris')
    print('La ciudad París',mensaje,'\nAhora la lista tiene un largo de',ciudades.index('Paris'))

# 20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista

print(ciudades.count('Buenos Aires'))
print(numeros.count(10))

# 21) Convertir la tupla en una lista

numeros_lista = list(numeros)
print(numeros)
print(numeros_lista)

# 22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables

primero, segundo, tercero,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_ = numeros
print(primero,segundo,tercero)

# 23) Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".

ciudades_23 = ['Buenos Aires','Montevideo','Brasilia','Bogotá','Caracas']
ciudades_del_mundo = {'Ciudad':ciudades_23,'País':['Argentina','Ururguay'],'Continente':['América','Europa']}
print(ciudades_del_mundo)

# 24) Imprimir las claves del diccionario

print(ciudades_del_mundo.keys())

# 25) Imprimir las ciudades a través de su clave

print(ciudades_del_mundo['Ciudad'])