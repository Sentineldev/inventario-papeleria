#Clase/Objeto para generar la tablaHash
class Tablahash:
    #Metodo constructor, que inicializa una matriz con el tamaño que se le indique, de forma que se puedan controlar las colisiones
    def __init__(self):
        self.max_tam = 1000
        self.lista = [[] for i in range(self.max_tam)]

    #Generando el indice por medio de la tecnica de hashing de 'Resto de la division' utilizando el tamaño del arreglo como divisor
    def Hash(self,clave):
        indice = 0
        for caracter in clave:
            indice += ord(caracter)
        return indice % self.max_tam

    #Agregando el elemento a la lista luego de generar el indice con la tecnica de hash    
    def agregar_elemento(self,clave,valor):
        indice = self.Hash(clave)
        encontrado = False
        for elemento in self.lista[indice]:
            if elemento[0] == clave:
                encontrado  = True
        if not encontrado:
            self.lista[indice].append([clave,valor])
        else:
            return encontrado                
    #Buscar un elemento con la clave proporcionada
    def buscar_elemento(self,clave):
        indice = self.Hash(clave)
        encontrado = False
        for index,elemento in enumerate(self.lista[indice]):
            if elemento[0] == clave:
                return elemento[1],(indice,index)
                encontrado = True
            else:
                encontrado = False
        return encontrado
    #Borrar un elemento con la clave proporcionada
    def borrar_elemento(self,clave):
        indice = self.Hash(clave)
        for index,elemento in enumerate(self.lista[indice]):
            if elemento[0] == clave:
                del self.lista[indice][index]

