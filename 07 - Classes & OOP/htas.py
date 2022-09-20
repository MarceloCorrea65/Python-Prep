class htas:
    def __init__(self, lista):
        self.lista = lista

    def es_primo(self):
        for i in self.lista:
            if (self.__es_primo(i)):
                print('El elemento', i, 'SI es un numero primo')
            else:
                print('El elemento', i, 'NO es un numero primo')

    def __es_primo(self, num):
        for h in range(2, num-1):
            if (num % h) == 0:
                return False
        return True

    def valor_modal(self, menor):
        lista_unicos = []
        lista_repeticiones = []
        if len(self.lista) == 0:
            return None
        if (menor):
            self.lista.sort()
        else:
            self.lista.sort(reverse=True)
        for elemento in self.lista:
            if elemento in lista_unicos:
                i = lista_unicos.index(elemento)
                lista_repeticiones[i] += 1
            else:
                lista_unicos.append(elemento)
                lista_repeticiones.append(1)
        moda = lista_unicos[0]
        maximo = lista_repeticiones[0]
        for i, elemento in enumerate(lista_unicos):
            if lista_repeticiones[i] > maximo:
                moda = lista_unicos[i]
                maximo = lista_repeticiones[i]
        return moda, maximo

    def conversion_grados(self, origen, destino):
        for i in self.lista:
            print(i, 'grados', origen, 'son', self.__conversion_grados(i, origen, destino),'grados',destino)

    def __conversion_grados(self, lista, origen, destino):
        valor_destino = None
        if (origen == 'celsius'):
            if (destino == 'celsius'):
                valor_destino = lista
            elif (destino == 'farenheit'):
                valor_destino = (lista * 9 / 5) + 32
            elif (destino == 'kelvin'):
                valor_destino = lista + 273.15
            else:
                print('Parámetro de Destino incorrecto')
        elif (origen == 'farenheit'):
            if (destino == 'celsius'):
                valor_destino = (lista - 32) * 5 / 9
            elif (destino == 'farenheit'):
                valor_destino = lista
            elif (destino == 'kelvin'):
                valor_destino = ((lista - 32) * 5 / 9) + 273.15
            else:
                print('Parámetro de Destino incorrecto')
        elif (origen == 'kelvin'):
            if (destino == 'celsius'):
                valor_destino = lista - 273.15
            elif (destino == 'farenheit'):
                valor_destino = ((lista - 273.15) * 9 / 5) + 32
            elif (destino == 'kelvin'):
                valor_destino = lista
            else:
                print('Parámetro de Destino incorrecto')
        else:
            print('Parámetro de Origen incorrecto')
        return valor_destino

    def factorial(self):
        for i in self.lista:
            print('El factorial de ', i, 'es', self.__factorial(i))


    def __factorial(self, numero):
        if(type(numero) != int):
            return 'El numero debe ser un entero'
        if(numero < 0):
            return 'El numero debe ser pisitivo'
        if (numero > 1):
            numero = numero * self.__factorial(numero - 1)
        return numero