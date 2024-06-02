import json
from datos import *
def registrar_usuario(datos_estudiantes_inscritos):
    Usuario={}
    doc= input("Ingrese su numero de documento")
    if doc in datos_estudiantes_inscritos:
        print("esite")            
    else: 
        Usuario["nombres"] = input("ingrese sus nombre: ")
        Usuario["Apellidos"] = input("ingrese sus apellidos: ")
        Usuario["direccion"] = input("ingrese su direccion: ")
        Usuario["Edad"] = input("ingrese su edad: ")
        Usuario["Acudiente"] = input("ingrese su acudiente: ")
        Usuario["celular"] = input("ingrese su celular: ")
        Usuario["telefono"] = input("ingrese su telefono: ")
        Usuario["estado"] = "no"
        Usuario["riesgo"] = False
        Usuario["aprobo"] = "no definida"
        Usuario["nota"] = 0
        datos_estudiantes_inscritos[doc]=Usuario
        return datos_estudiantes_inscritos
    print("guardado con exito")

    print(datos_estudiantes_inscritos)
    
    #medio