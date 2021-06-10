#Importar los modulos necesarios
from tablahash import Tablahash
from articulo import Articulo
from validaciones import validar_cadena_alfanumerica,validar_numero_entero,validar_cadena
from sys import exit



#Genera una tabla hash segun los registros obtenidos
def generar_tabla_hash(registros):
    articulos = Tablahash()
    #Genera un indice para cada registro segun la referencia
    for elemento in registros:
        articulos.agregar_elemento(elemento.referencia,elemento)
    return articulos

#Se cargan los registros que se encuentran en el archivo .txt
def cargar_registros():
    registros = []
    try: # Si no sucede una expecion, se leen las lineas
        for line in open('ARTICULOS.txt','r'): #Cada linea del archivo
            if '*' in line.split(',')[0]: #Verifica que no haya sido eliminado (que tenga * al final)
                continue
            #Divide la linea y se les asigna en los parametros de abajo
            referencia,distribuidora,nombre_art,cantidad_art,precio,fecha_salida = line.split(',') 
            fecha_salida = fecha_salida.split('/') #La fecha se separa (volviendo un arreglo de string)
            #La fecha se reagrupa indicando dia, mes y año
            fecha_salida = { "Dia":fecha_salida[0] , "Mes":fecha_salida[1], "Año":fecha_salida[2].split('\n')[0]}
            # Se genera el articulo
            articulo = Articulo(referencia,distribuidora,nombre_art,cantidad_art,precio,fecha_salida)
            registros.append(articulo)
    except:
        file = open('ARTICULOS.txt','x')
        file.close()
    
    # Se generan la tabla hash de todos los registros
    articulos = generar_tabla_hash(registros)
    return articulos

#Se actualiza la informacion del archivo, cuando se haga insercion,modificacion o eliminacion de un registro
def actualizar_archivo(inventario):
    file = open('ARTICULOS.txt','w')
    for lista in inventario.lista: #Para cada elemento del arreglo
        if len(lista) > 0:
            for articulo in lista: #Para cada articulo
                #Escribe en el archivo lo correspodiente
                file.write(
                    articulo[1].referencia+','+articulo[1].distribuidora+','+articulo[1].nombre_art+','+articulo[1].cantidad_art+','+articulo[1].precio+','+articulo[1].fecha_salida["Dia"]+'/'+articulo[1].fecha_salida["Mes"]+'/'+articulo[1].fecha_salida["Año"]+'\n'
                )
        
    file.close()
    inventario = cargar_registros()
    return inventario

# Opcion 6: se listan los registros que tengan una fecha del 2020
def listar_vendidos_fecha(fecha,inventario):
    for lista in inventario.lista:
        if len(lista) > 0:
            for articulo in lista:
                if int(articulo[1].fecha_salida["Año"]) == fecha:
                    articulo[1].mostrar_articulo()
    input('\nPresione enter para volver al menu')

# Opcion 5: se listan los articulos que tienen una cantidad en inventario mayor a 0
def listar_articulos_disponibles(inventario):
    for lista in inventario.lista:
        if len(lista) > 0:
            for articulo in lista:
                if int(articulo[1].cantidad_art) > 0:
                    articulo[1].mostrar_articulo()
    input('\nPresione enter para volver al menu.')

# Opcion 3: Modifica un registro
# NOTA: Aqui solo se busca la referencia, las modificaciones se realizan en articulo.py
def modificar_articulo(inventario):
    referencia = input('Indique referencia del articulo a modificar: ')
    validar_referencia = validar_cadena_alfanumerica(referencia,10)
    while validar_referencia["status"] == False:
        print(validar_referencia["error_message"])
        referencia = input('Indique referencia del articulo a modificar: ')
        validar_referencia = validar_cadena_alfanumerica(referencia,10)
    if inventario.buscar_elemento(referencia) != False:  
        articulo_indice = inventario.buscar_elemento(referencia)[1]
        inventario.lista[articulo_indice[0]][articulo_indice[1]][1].modificar_articulo() #Continua en articulo.py
        actualizar_archivo(inventario)
        input('Presione enter para volver al inicio')
        #articulo.referencia = input('Nueva referencia: ')
        #inventario.borrar_elemento(referencia)
        #inventario.agregar_elemento(articulo.referencia,articulo)
        #actualizar_archivo(inventario)
    else:
        print('\n<--Articulo no encontrado-->\n')
        input('Presione enter para volver al inicio')

# Opcion 4: Se modifica la cantidad de existencia de un articulo en el inventario
def registrar_venta_compra_articulo(inventario):
    referencia = input('Indique la referencia del articulo: ') #Se toma la referencia del articulo
    tipo_modificacion = None
    if inventario.buscar_elemento(referencia) != False: #Se busca el articulo dentro del arreglo
        print('\n1. Compra')  #Opciones para saber si se sumara o restara de la cantidad de existencia
        print('2. Venta\n')
        tipo_modificacion = input('\nDigite una opcion: ')
        validar_entrada_cadena = validar_numero_entero(tipo_modificacion) #se valida que sea un numero el que introduzca el usuario
        while validar_entrada_cadena["status"] == False: #mientras no sea un numero se repetira
            print(validar_entrada_cadena["error_message"])
            tipo_modificacion = input('\nDigite una opcion: ')
            validar_entrada_cadena = validar_numero_entero(tipo_modificacion)
        
        tipo_modificacion = int(tipo_modificacion)
        articulo_indice = inventario.buscar_elemento(referencia)[1] #se toma el indice donde se encuentra el registro dentro del arreglo
        inventario.lista[articulo_indice[0]][articulo_indice[1]][1].mostrar_articulo() #mostrando los datos del articulo
        cantidad_art = input('\nIngrese la cantidad de articulos: ')
        
        validar_cantidad_art = validar_numero_entero(cantidad_art)
        while validar_cantidad_art["status"] == False: #mientras no sea un numero entero se repetira
            print(validar_cantidad_art["error_message"])
            cantidad_art = input('\nIngrese la cantidad de articulos: ')
            validar_cantidad_art = validar_numero_entero(cantidad_art)
        
        cant_actual = int(inventario.lista[articulo_indice[0]][articulo_indice[1]][1].cantidad_art) #se toma la cantidad actual del registro
        cantidad_art = int(cantidad_art) #cantidad que se añadira
        
        if tipo_modificacion == 1: #validar si es suma o resta lo que se realizara
            nueva_cantidad = cantidad_art+cant_actual
        else:
            if cant_actual < cantidad_art: #se debe vender una cantidad menor a la que esta en existencia
                input('No puedes vender mas de lo que tienes, presiona enter pasa salir')
                return 0
            nueva_cantidad = cant_actual-cantidad_art
            inventario.lista[articulo_indice[0]][articulo_indice[1]][1].registrar_fecha_salida()
        nueva_cantidad = str(nueva_cantidad) #se convierte a string para guardarse en el archivo
        inventario.lista[articulo_indice[0]][articulo_indice[1]][1].cantidad_art = nueva_cantidad #se le añade la nueva cantidad al registro
        actualizar_archivo(inventario) # seactualiza el archivo y el arreglo

    else:
        input('<--El articulo no esta registrado, pulse enter para volver al inicio-->')

# Opcion 7: se elimina un registro del arreglo y se marca con un * en el archivo de datos
def eliminar_articulo(inventario):
    referencia = input('Indique la referencia del articulo: ')
    if inventario.buscar_elemento(referencia) != False: #El articulo debe existir
        articulo_indice = inventario.buscar_elemento(referencia)[1]
        inventario.lista[articulo_indice[0]][articulo_indice[1]][1].referencia+='*' #la referencia se marca con *
        actualizar_archivo(inventario)
        print('Articulo eliminado exitosamente')
    else:
        print('No existe el articulo')
    input('<--pulse enter para volver al inicio-->')

# Opcion 2: agregar un registro al arreglo y al archivo de datos.
# NOTA: Aqui solo valida la referencia. El resto se inserta en articulo.py
def agregar_articulo(inventario):
    referencia = input('Ingrese la referencia: ')
    validar_referencia = validar_cadena_alfanumerica(referencia,10)
    while validar_referencia["status"] == False:
        print(validar_referencia["error_message"])
        referencia = input('Ingrese la referencia: ')
        validar_referencia = validar_cadena_alfanumerica(referencia,10)
    if inventario.buscar_elemento(referencia):
        print('\n<--Ya se encuentra registrado-->')
        input('\nPresione enter para volver al inicio')
    else:
        articulo = Articulo()
        articulo.registrar_articulo(referencia) #Continua en articulo.py
        file = open('ARTICULOS.txt','a')
        file.write(
            articulo.referencia+','+articulo.distribuidora+','+articulo.nombre_art+','+articulo.cantidad_art+','+articulo.precio+','+articulo.fecha_salida["Dia"]+'/'+articulo.fecha_salida["Mes"]+'/'+articulo.fecha_salida["Año"]+'\n'
        )
        file.close()
        inventario.agregar_elemento(articulo.referencia,articulo)

# Opcion 1: buscar y mostrar informacion sobre un articulo
def consultar_articulo(inventario):
    referencia = input('\nIngrese la referencia: ') #se toma la referencia
    validar_referencia = validar_cadena_alfanumerica(referencia,10)
    while validar_referencia["status"] == False:
        print('\n'+validar_referencia["error_message"]+'\n')
        referencia = input('Ingrese la referencia: ')
        validar_referencia = validar_cadena_alfanumerica(referencia,10)
    if inventario.buscar_elemento(referencia): #se valida que el registro exista
        articulo = inventario.buscar_elemento(referencia) #si existe se musetra
        articulo,articulo_posicion = articulo[0],articulo[1]
        articulo.mostrar_articulo()
        input('\n\t<--Presione enter para volver al menu-->')
    else:
        input('\n\tEl articulo no existe, <--Presiona una tecla para volver al menu-->')

#menu de opciones
def menu(inventario):
    opc = None 
    while opc != 0:
        inventario = actualizar_archivo(inventario) #el archivo es actualizado y el arreglo cada vez que se muestra el menu
        print('\n\t..:PAPELERIA LA PRINCIPAL ESTACION:..\n')
        print('[1]. Consultar articulo')
        print('[2]. Agregar articulo')
        print('[3]. Modificar un articulo')
        print('[4]. Registrar venta o compra de un articulo')
        print('[5]. Listar articulos disponibles')
        print('[6]. Listar articulos vendidos en el 2020')
        print('[7]. Eliminar articulo')
        print('[0]. Salir del programa')
        opc = input('\n\t\tIngrese una opcion: ')
        try: #La opcion debe ser un numero, si sucede una excepcion, no lo es
            opc = int(opc)
        except:
            print('\n<--Error ingrese solo numeros-->\n')
            opc = input('Ingrese una opcion: ')

        if opc == 1: #Consulta
            consultar_articulo(inventario)
        elif opc == 2: #Agregar
            agregar_articulo(inventario)
        elif opc == 3: #Modificar
            modificar_articulo(inventario)
        elif opc == 4: #Compra/Venta
            registrar_venta_compra_articulo(inventario)
        elif opc == 5: #Listar
            listar_articulos_disponibles(inventario)
        elif opc == 6: #Listar vendidos 2020
            listar_vendidos_fecha(2020,inventario)
        elif opc == 7: # Eliminar
            eliminar_articulo(inventario)
        elif opc == 0: # Salir
            exit()


def run_app():
    inventario = cargar_registros() #al iniciar el programa se lee los archivos que esten dentro del archivo de texto y borrando los que esten marcando con *
    menu(inventario)