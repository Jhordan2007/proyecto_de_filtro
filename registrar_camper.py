import json
from datos import *
def registrar_usuario(datos):
    Usuario={}
    doc= input("Ingrese su numero de documento")
    if doc in datos["usuarios"]:
        print("esite")            
    else: 
        Usuario["nombres"] = input("ingrese sus nombre: ")
        Usuario["Apellidos"] = input("ingrese sus apellidos: ")
        Usuario["direccion"] = input("ingrese su direccion: ")
        Usuario["Edad"] = input("ingrese su edad: ")
        Usuario["Acudiente"] = input("ingrese su acudiente: ")
        Usuario["celular"] = input("ingrese su celular: ")
        Usuario["telefono"] = input("ingrese su telefono: ")
        Usuario["estado"] = False
        Usuario["riesgo"] = False
        datos[doc]=Usuario

        print("guardado con exito")

    print(datos)
    
    #medio