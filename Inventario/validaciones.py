# Libreria de validaciones

# Verifica si una cadena solo contiene letras y numeros y que este no se pase del limite de letras
def validar_cadena_alfanumerica(cadena_alfanumerica,max_tam):
    #Que no se pase del tamaño
    if len(cadena_alfanumerica) <= max_tam and len(cadena_alfanumerica) > 0:
        contador_letra = 0
        contador_numero = 0
        for caracter in cadena_alfanumerica: #Cada caracter de la cadena
            if ord(caracter) > 64 and ord(caracter) < 91 or ord(caracter) > 96 and ord(caracter) < 123: #Letras
                contador_letra+=1
            elif ord(caracter) > 47 and ord(caracter) < 58: #0-9
                contador_numero+=1
            elif caracter == ' ':
                contador_letra+=1
            else:
                return {"error_message":'Error ingrese solo numeros o letras',"status":False}
        
        #Solo cuenta si tiene numeros y letras, si hay un caracter diferente, habran menos letras y numeros de lo que deberia tener
        if contador_letra+contador_numero == len(cadena_alfanumerica): 
            return {"error_message":None,"status":True}
        else:
            return {"error_message":f"Error introduzca denuevo, debe contener solo numeros y letras","status":False}
    else:
        return {"error_message":f"El nombre del articulo o la referencia debe ser menor o igual  a {max_tam} caracteres","status":False}




#Verifica que una cadena solo contenga letras y que este no se pase del limite
def validar_cadena(distribuidora):
    contador_caracteres = 0
    max_tam = 30
    if len(distribuidora)<= max_tam:
        for caracter in distribuidora: #Cada caracter de la cadena
            if ord(caracter) > 64 and ord(caracter) < 91 or ord(caracter) > 96 and ord(caracter)< 123: #Letras
                contador_caracteres+=1
            elif caracter == ' ':
                contador_caracteres+=1
        if contador_caracteres == len(distribuidora):
            return {"error_message":None,"status":True}
        else:
            return {"error_message":"Debe indicar solo letras","status":False}
    else:
        return {"error_message":"El nombre de la distribuidora debe ser menor o igual  a 25 caracteres","status":False}




#Verifica si la fecha es valida
def validar_fecha(fecha):
    #Verifica que la fecha sea un numero
    if validar_numero_entero(fecha["dia"]) and validar_numero_entero(fecha["mes"]) and validar_numero_entero(fecha["año"]):
        fecha["dia"],fecha["mes"],fecha["año"] = int(fecha["dia"]),int(fecha["mes"]),int(fecha["año"])
        #El dia esta entre 1-31
        if fecha["dia"] > 0 and fecha["dia"] < 32:
            #El mes esta entre 1-12
            if fecha["mes"] > 0 and fecha["mes"] < 13:
                #El año es superior a 0
                if fecha["año"] > 0:
                    return {'error_message':None,"status":True}
                else:
                    return {'error_message':'El año debe ser mayor a 0',"status":False}
            else:
                return {'error_message':'El mes debe ser mayor a 0 y menor que 13',"status":False}
        else:
            return {'error_message':'El dia debe ser mayor a 0 y menor que 32',"status":False}
    else:
        return {'error_message':'Introduzca solo numeros en la fecha',"status":False}


#Verifica que el valor sea un numero
def validar_numero_entero(numero):
    numero = str(numero)
    valido = False
    for caracter in numero: #Cada caracter de la cadena
        if ord(caracter) > 47 and ord(caracter) < 58: #Cada caracter debe ser de 0 a 9
            valido = True
        else:
            valido = False
    if valido == True:
        return {"error_message":None,"status":True}
    else:
        return {"error_message":"Debe indicar un numero entero","status":False}
        
#Verifica que el valor sea un numero mayor a 0
def validar_entero_positivo(numero):
    try: #Si no lanza una expecion, es un numero
        if int(numero) >= 0: # Debe ser mayor a 0
            return {"error_message":None,"status":True}
        else:
            return {"error_message":"El numero debe ser mayor a cero","status":False}
    except:
        return {"error_message":"Debe indicar un numero entero","status":False}

#Verifica que el valor sea un numero decimal
def validar_numero_decimal(numero):
    try: #Si no lanza una expecion, es un numero decimal
        numero = float(numero)
        return {"error_message":None,"status":True}
    except:
        return {"error_message":"Debe indicar un numero decimal","status":False}

#Verifica que el valor sea un numero decimal mayor a 0
def validar_decimal_positivo(numero):
    try: #Si no lanza una expecion, es un numero decimal
        if float(numero) >= 0: # Debe ser mayor a 0
            return {"error_message":None,"status":True}
        else:
            return {"error_message":"El numero debe ser mayor a cero","status":False}
    except:
        return {"error_message":"Debe indicar un numero decimal","status":False}

#validar una fecha con el formato DD/MM/AA

def validar_fecha(fecha):
    try:
        fecha_validar = fecha.split('/')
        if validar_entero_positivo(fecha_validar[0])["status"]:
            if validar_entero_positivo(fecha_validar[1])["status"]:
                if validar_entero_positivo(fecha_validar[2])["status"]:
                    return validar_entero_positivo(fecha_validar[2])
                else:
                    return validar_entero_positivo(fecha_validar[2])
            else:
                return validar_entero_positivo(fecha_validar[1])
        else:
            return validar_entero_positivo(fecha_validar[0])
    except:
        return {"error_message":"Fecha invalida","status":False}

#Validar un registro en la aplicacion con interfaz grafica

def validar_registro(referencia,distribuidora,nombre_art,cantidad_art,precio,fecha):
    if validar_cadena_alfanumerica(referencia,10)["status"]:
        if validar_cadena(distribuidora)["status"]:
            if validar_cadena_alfanumerica(nombre_art,25)["status"]:
                if validar_entero_positivo(cantidad_art)["status"]:
                    if validar_decimal_positivo(precio)["status"]:
                        if validar_fecha(fecha)["status"]:
                            return validar_fecha(fecha)
                        else:
                            return validar_fecha(fecha)
                    else:
                        return validar_decimal_positivo(precio)
                else:
                    return validar_entero_positivo(cantidad_art)
            else:
                return validar_cadena_alfanumerica(nombre_art,25)
        else:
            return validar_cadena(distribuidora)
    else:
        return validar_cadena_alfanumerica(referencia,10)



