from programa import run_app as programa
from programa_consola import run_app as console_programa
from validaciones import validar_entero_positivo


"""
PROYECTO REALIZADO POR:
    Cesar Zabala
    Jesus Figuera
    Ulises Hernandez
"""

if __name__ == '__main__':
    print("<-----------Autores: Jesus Figuera - Cesar Zabala - Ulises Hernadez---------->")
    print("\n\t..:Papeleria La Primera Estacion:..")
    print("\nComo deseas correr el programa?\n")
    print("[1]. Con interfaz grafica")
    print("[2]. Por consola")
    print("[0]. Salir")
    opc = input("\nIngrese una opcion: ")
    while validar_entero_positivo(opc)["status"] == False:
        print(validar_entero_positivo(opc)["error_message"])
        opc = input("Ingrese una opcion: ")
    opc = int(opc)
    if opc == 1:
        programa()
    elif opc == 2:
        console_programa()
    else:
        print("<--Hasta luego-->")