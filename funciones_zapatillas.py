
def menu_zapas():
    menu = """
========= reserva de zapatilas =========
    
1.- Reservar zapatillas
2.- Buscar zapatillas reservadas.
3.- Cancelar reserva de zapatillas.
4.- Salir.

"""
   #inicializa el menu 
    while True:
        print(menu)
         #pide al usuario ingresar una opcion 
        opt=input("Ingresa una opcion del (1 al 4)\n:")

        if opt =="1":
            Reservar_zapatillas()
        elif opt=="2":
            Buscar_zapatillas_reservadas()
        elif opt=="3":
            Cancelar_reserva_zapatillas()
        elif opt=="4":
            print("Gracias por usar el programa adios!")
            break
        else:
            print("Error! Opcion incorrecta debes elegir del 1 al 4")



reservas_activas=[]
stock=20
#debe tene un stock maximo de 20 el usuario no puede seleccionar mas de uno y el nombre no puede estar repetido usar un diccionario y comando list o value() para convertirlo
def Reservar_zapatillas():
    global stock
    print("Sistema de reserva")
    nombre=validar_texto("Ingresa Tu nómbre\n:")
    
    codigo=input("Ingresa el codigo este codigo exactamente igual( EstoyEnListaDeReserva )\n:")
    codigo_user="EstoyEnListaDeReserva"
    if codigo == codigo_user:
        print("Procesando la reseverva........")
        stock-=1
        if stock == 0:
            print("no hay stock")
            return
        if nombre in reservas_activas:
            print("Ya esta registrado este usuario!")
            return
    else:
        print("debes escribirlo exactamente igual")
        return
    print("reserva exitosa!")
    reserva={
        "nombre"  : nombre,
        "codigo"  : codigo
    }
    reservas_activas.append(reserva)
   

def Buscar_zapatillas_reservadas():
    global stock
    print("Busqueda de usuarios reservados")
    user=validar_texto("Ingresa el nombre del usuario\n: ")
    for t in reservas_activas:
        
        if user == t:
            print(f"nombre: {t[0]}")
            vip=input("Desea una reserva vip le permite reservar una zapatilla adicional (s/n)\n:")
            if vip == "s":
                if stock == 0:
                    print("no hay stock")
                    return
                else:
                    stock-=1
                print("Reserva vip exitosa!")
            else:
                print("Gracias por su preferencia")
    print("usuario no encontrado")

def Cancelar_reserva_zapatillas():
    print("eliminacion de usuarios reservados")
    user_name=validar_texto("Ingrese el nombre del usuario: ")
    for t in reservas_activas:
        if user_name == t:
            reservas_activas.pop(t)
            print("Usuario eliminado con exito!")
    print("Usuario no encontrado!")        



def validar_texto(mensaje):
    while True:
        texto = input(mensaje).strip().lower()
        if len(texto)>=3:
            return texto
        print("Error! debe escribir al menos 3 caracteres!")