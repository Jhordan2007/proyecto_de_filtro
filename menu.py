from registrar_camper import *
from datos import *
from coordinador_config import *

RUTA_DATOS_ESTUDIANTESINSC = "estudiantes_inscritos.json"
datos_estudiantes_inscritos = cargar_datos(RUTA_DATOS_ESTUDIANTESINSC)

RUTA_DATOS_ESTUDIANTESCURS = "estudiantes_Cursando.json"
datos_estudiantes_Cursando = cargar_datos(RUTA_DATOS_ESTUDIANTESCURS)

print(datos_estudiantes_inscritos)



while True:
    print("----------------------------------------------------------------")
    print("Bievenido a la plataforma de campuslands")
    print("1. Registrarse")
    print("2. Ingresar como camper")
    print("3. Ingresar como trainer")
    print("4. ingresar como coordinador")
    print("5. Usuarios")
    print("----------------------------------------------------------------")
    opc = int(input("Ingrese la opciòn que deseas--> "))
    if opc == 1:
        registrar_usuario(datos_estudiantes_inscritos)
    elif opc == 2:
      menu_coordinador()
    elif opc == 4:
       menu_coordinador()
    elif opc == 0:
       break    









    guardar_datos(datos_estudiantes_inscritos, RUTA_DATOS_ESTUDIANTESINSC)
    guardar_datos(datos_estudiantes_Cursando,RUTA_DATOS_ESTUDIANTESCURS)