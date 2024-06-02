import json
from datos import *

RUTA_DATOS_ESTUDIANTESCURS = "estudiantes_Cursando.json"
datos_estudiantes_Cursando = cargar_datos(RUTA_DATOS_ESTUDIANTESCURS)

RUTA_DATOS_ESTUDIANTESINSC = "estudiantes_inscritos.json"
datos_estudiantes_inscritos = cargar_datos(RUTA_DATOS_ESTUDIANTESINSC)

RUTA_DATOS_RUTA = "rutas.json"
datos_de_ruta = cargar_datos(RUTA_DATOS_RUTA)

RUTA_DATOS_TRAINERS = "trainers.json"
datos_trainers= cargar_datos(RUTA_DATOS_TRAINERS)

def Aprobo_o_no(datos_estudiantes_cursando):
    print(datos_estudiantes_cursando)
    doc= input("Ingrese el numero del documento del usuario")
    if doc in datos_estudiantes_cursando:
        print("usuario encontrado")
        print(datos_estudiantes_cursando[doc]["nota"])
    datos_estudiantes_cursando[doc]["aprobo"]=input("Ingresa si aprobo o no aprobo")
    guardar_datos(datos_estudiantes_cursando,RUTA_DATOS_ESTUDIANTESCURS)
def agregar_trainer(datos_trainers):
    Trainers={}
    Trainer= input("Ingrese el nombre del trainer")
    if Trainer in datos_trainers:
        print("esite")
    else:
        datos_trainers[Trainer]=Trainers
        guardar_datos(datos_trainers,RUTA_DATOS_TRAINERS)
    print(datos_trainers)

def agregar_ruta(datos):
    rutas={}
    ruta= input("Ingrese la ruta que desea agregar")
    if ruta in datos:
        print("esite")
        
    else:
        datos[ruta]=rutas
        guardar_datos(datos,RUTA_DATOS_RUTA)
    print(datos)

def usuario_pendiente(datos_estudiantes_inscritos):
    print(datos_estudiantes_inscritos)
    doc= input("Ingrese el numero del documento del usuario")
    if doc in datos_estudiantes_inscritos:
        print("usuario encontrado")
        datos_estudiantes_inscritos[doc]["estado"]=True
        print("aceptado")
        guardar_datos(datos_estudiantes_inscritos,RUTA_DATOS_ESTUDIANTESINSC) 
    if datos_estudiantes_inscritos[doc]["estado"]==True:
        guardar_datos(datos_estudiantes_inscritos,RUTA_DATOS_ESTUDIANTESCURS)

def editar_usuarios(datos_estudiantes_Cursando):
    doc= input("Ingrese su numero de documento: ")
    if doc in datos_estudiantes_Cursando["estudiantes"]:
        print("usuario encontrado")
        datos_estudiantes_Cursando["estudiantes"][doc]["nombres"]=input("Ingrese NUEVO nombre: ")
        datos_estudiantes_Cursando["estudiantes"][doc]["apellidos"]=input("Ingrese NUEVOS apellidos: ")
        datos_estudiantes_Cursando["estudiantes"][doc]["Direccion"]=input("Ingrese NUEVA DIRECCION : ")
        datos_estudiantes_Cursando["estudiantes"][doc]["Edad"]=int(input("Ingrese Nueva edad: "))
        datos_estudiantes_Cursando["estudiantes"][doc]["acudiente"]=input("Ingrese NUEVO NOMBRE de acudiente: ")
        datos_estudiantes_Cursando["estudiantes"][doc]["Celular"]=input("Ingrese NUEVO NUMERO de celular: ")
        datos_estudiantes_Cursando["estudiantes"][doc]["telefono fijo"]=int(input("Ingrese NUEVO NUMERO telefono fijo: "))
        datos_estudiantes_Cursando["estudiantes"][doc]["Estado"]="cursando"
        datos_estudiantes_Cursando["estudiantes"][doc]["riesgo"]= False
        guardar_datos(datos_estudiantes_Cursando,RUTA_DATOS_ESTUDIANTESCURS)
        





def menu_coordinador():
    print("----------------------------------------------------------------")
    print("Bienvenido al menu coordinador")
    print("1. Editar usuarios")
    print("2. Aceptar usuarios pendientes")
    print("3. Agregar ruta")
    print("4. Agregar Trainer")
    print("5. Decir si aprueba o no.")
    print("----------------------------------------------------------------")
    
    while True:
        opc = int(input("Ingrese la opciòn que deseas--> "))
        if opc == 1:
            editar_usuarios(datos_estudiantes_Cursando) 
        elif opc == 2:
            usuario_pendiente(datos_estudiantes_inscritos)
        elif opc == 3:
            agregar_ruta(datos_de_ruta)
        elif opc == 4:
            agregar_trainer(datos_trainers)
        elif opc == 5:
            Aprobo_o_no(datos_estudiantes_Cursando)
        
        
        elif opc == 0:
            break
#medi