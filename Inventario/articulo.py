from validaciones import *

# Clase/objeto Articulo, donde contiene sus datos
class Articulo:
    
    #Constructor, asigna las respectivas variables que se pasan con los parametros
    def __init__(self,referencia=None,distribuidora=None,nombre_art=None,cantidad_art=None,precio=None,fecha_salida=None):
        self.referencia = referencia
        self.distribuidora = distribuidora
        self.nombre_art = nombre_art
        self.cantidad_art = cantidad_art
        self.precio = precio
        self.fecha_salida = fecha_salida
    
    # Registra un articulo, continua de la opcion 2 del main.py
    def registrar_articulo(self,referencia):
        #Distribuidora
        self.distribuidora = input('Ingrese la distribuidora: ')
        validar_distribuidora = validar_cadena(self.distribuidora)
        while validar_distribuidora["status"] == False: 
            print(validar_distribuidora["error_message"])
            self.distribuidora = input('Ingrese la distribuidora: ')
            validar_distribuidora = validar_cadena(self.distribuidora)
        #Nombre
        self.nombre_art = input('Ingrese nombre del articulo: ')
        validar_nombre_art = validar_cadena_alfanumerica(self.nombre_art,30)
        while validar_nombre_art["status"] == False:
            print(validar_nombre_art["error_message"])
            self.nombre_art = input('Ingrese nombre del articulo: ')
            validar_nombre_art = validar_cadena_alfanumerica(self.nombre_art,30)
        #Cantidad
        self.cantidad_art = input('Ingrese la cantidad del articulo en inventario: ')
        validar_cantidad = validar_entero_positivo(self.cantidad_art)
        while validar_cantidad["status"] == False:
            print(validar_cantidad["error_message"])
            self.cantidad_art = input('Ingrese la cantidad del articulo en inventario: ')
            validar_cantidad = validar_entero_positivo(self.cantidad_art)
        #Precio
        self.precio = input('Ingrese el precio del articulo: ')
        validar_precio = validar_decimal_positivo(self.precio)
        while validar_precio["status"] == False:
            print(validar_precio["error_message"])
            self.precio = input('Ingrese el precio del articulo: ')
            validar_precio = validar_decimal_positivo(self.precio)

        self.referencia = referencia
        
        # Como aun no se ha vendido, no hay fecha de salida
        self.fecha_salida = {"Dia":'0',"Mes":'0',"Año":'0'}
        
        
    
    # Registra la fecha de salida de un articulo
    def registrar_fecha_salida(self):
        print('\n\tFecha de salida del articulo\n')
        #Dia
        dia = input('Dia: ')
        validar_dia = validar_numero_entero(dia)
        while validar_dia["status"] == False:
            print(validar_dia["error_message"])
            dia = input('Dia: ')
            validar_dia = validar_numero_entero(dia)
        #Mes
        mes = input('Mes: ')
        validar_mes = validar_numero_entero(mes)
        while validar_mes["status"] == False:
            print(validar_mes["error_message"])
            mes = input('Mes: ')
            validar_mes = validar_numero_entero(mes)
        #Año
        ano = input('Año: ')
        validar_ano = validar_numero_entero(ano)
        while validar_ano["status"] == False:
            print(validar_ano["error_message"])
            ano = input('Año: ')
            validar_ano = validar_numero_entero(ano)
        #Se registra la fecha de salida
        self.fecha_salida = {"Dia":dia,"Mes":mes,"Año":ano}
    
    # Muestra el articulo
    def mostrar_articulo(self):
        print('\n\t..:INFORMACION DEL ARTICULO:..\n')
        print(f'Referencia: {self.referencia}')
        print(f'Distribuidora: {self.distribuidora}')
        print(f'Nombre: {self.nombre_art}')
        print(f'Cantidad en inventario: {self.cantidad_art}')
        print(f'Precio: {self.precio}$')
        print(f'Fecha de salida: {self.fecha_salida["Dia"]}/{self.fecha_salida["Mes"]}/{self.fecha_salida["Año"]}')
    
    # Abre un menu para modificar el articulo
    def modificar_articulo(self):
        print('\n\t..:MODIFICAR ARTICULO:..')
        print('[1]. Modificar referencia')
        print('[2]. Modificar distribuidora')
        print('[3]. Modificar nombre del articulo')
        print('[4]. Modificar precio')
        print('[5]. Modificar cantidad del articulo en inventario')
        print('[6]. Modificar fecha de salida del articulo ')
        opc = input('Digite una opcion: ')
        
        validar_opcion = validar_numero_entero(opc)
        while validar_opcion["status"] == False:
            print(validar_opcion["error_message"])
            opc = input('Digite una opcion: ')
            validar_opcion = validar_numero_entero(opc)
        
        opc = int(opc)
        #Modifica referencia
        if opc == 1:
            referencia = input('Indique la nueva referencia: ')
            validar_referencia = validar_cadena_alfanumerica(referencia,10)
            while validar_referencia["status"] == False:
                print(validar_referencia["error_message"])
                referencia = input('Indique la nueva referencia: ')
                validar_referencia = validar_cadena_alfanumerica(referencia,10)
            self.referencia = referencia
        #Modifica distribuidora
        elif opc == 2:
            distribuidora = input('Ingrese la distribuidora: ')
            validar_distribuidora = validar_cadena(distribuidora)
            while validar_distribuidora["status"] == False:
                print(validar_distribuidora["error_message"])
                distribuidora = input('Ingrese la distribuidora: ')
                validar_distribuidora = validar_cadena(distribuidora)
            self.distribuidora = distribuidora
        #Modifica nombre
        elif opc == 3:
            nombre_art = input('Ingrese nombre del articulo: ')
            validar_nombre_art = validar_cadena_alfanumerica(nombre_art,30)
            while validar_nombre_art["status"] == False:
                print(validar_nombre_art["error_message"])
                nombre_art = input('Ingrese nombre del articulo: ')
                validar_nombre_art = validar_cadena_alfanumerica(nombre_art,30)
            self.nombre_art = nombre_art
        #Modifica Precio
        elif opc == 4:
            precio = input('Ingrese el precio del articulo: ')
            validar_precio = validar_decimal_positivo(precio)
            while validar_precio["status"] == False:
                print(validar_precio["error_message"])
                precio = input('Ingrese el precio del articulo: ')
                validar_precio = validar_decimal_positivo(precio)
            self.precio = precio
        # Modifica cantidad
        elif opc == 5:
            cantidad_art = input('Ingrese la nueva  cantidad del articulo en inventario: ')
            validar_cantidad = validar_entero_positivo(cantidad_art)
            while validar_cantidad["status"] == False:
                print(validar_cantidad["error_message"])
                cantidad_art = input('Ingrese la nueva cantidad del articulo en inventario: ')
                validar_cantidad = validar_entero_positivo(cantidad_art)
            self.cantidad_art = cantidad_art
        # Modifica la fecha de salida
        elif opc == 6:
            self.registrar_fecha_salida()
        # Ninguna de las anteriores
        else:
            print('\n<--Opcion invalida-->\n')
    
    #Este metodo se utiliza pare registrar los articulos por medio de la interfaz grafica
    def registrar_articulov2(self,referencia,distribuidora,nombre_art,cantidad_art,precio,fecha_salida):
        self.referencia = referencia
        self.distribuidora = distribuidora
        self.nombre_art = nombre_art
        self.cantidad_art = cantidad_art
        self.precio = precio
        fecha_salida = fecha_salida.split('/')
        self.fecha_salida = {"Dia":fecha_salida[0],"Mes":fecha_salida[1],"Año":fecha_salida[2]}