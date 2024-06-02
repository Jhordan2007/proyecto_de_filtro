import json
from datos import *
RUTA_DATOS_ESTUDIANTESCURS = "estudiantes_Cursando.json"
datos_estudiantes_Cursando = cargar_datos(RUTA_DATOS_ESTUDIANTESCURS)

def mostrar_perfil(datos_estudiantes_cursando):
    doc= input("Ingrese su numero de documento")
    if doc in datos_estudiantes_cursando:
        print("usuario encontrado")
        print(datos_estudiantes_cursando[doc])
    else:
        print("no esite")
def menu_camper():
    print("----------------------------------------------------------------")
    print("Bienvenido al menu camper")
    print("1. Mostrar perfil")
    print("2. Mostrar notas")
    print("----------------------------------------------------------------")
    opc = int(input("Ingrese la opciòn que deseas--> "))
    if opc == 1:
        mostrar_perfil(datos_estudiantes_Cursando)
    elif opc == 2:
        print("2")