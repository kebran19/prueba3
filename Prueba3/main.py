# ------ NO BORRAR -----
from funciones import *
from herramientas import *
# ------ NO BORRAR -----

user = {}
menu = ["Revisar menú",
        "Revisar carrito",
        "Pagar",
        "Quitar item de carrito",
        "Buscar item en carrito por nombre",
        "Buscar item en carrito por ingredientes",
        "Filtrar items que den alergia",
        "Buscar ítem",
        "Modificar ítem del menú",
        "Agregar ítem al menú",
        "Guardar carrito",
        "Cargar carrito",
        "Calcular calorías",
        "Salir"]

#Acciones iniciales


#menu principal
#aca se muestra el menu principal
while (True):
    for i, opcion in enumerate(menu):
        print(f"{i+1}:{opcion}") #print(f"{i+1}:{opcion}") porque enumerate empieza en 0
    while True:
        acciones = int(input("Ingrese la acción a realizar: ")) #aca preguntamos que accion quiere realizar el usuario
        selecciones = menu[acciones-1] #menu[acciones-1] porque el usuario empieza en 1
        break
    print(selecciones) #aca se muestra la accion que se selecciono
    if acciones == 1: #se ejecuta primera accion (revisar menu)
        ver_menu(var)  #ejecutamos funcion ver_menu
        
    if acciones == 2: #se ejecuta segunda accion (revisar carrito)
        if carrito_user:
            print(carrito_user)
        else:
            print("El usuario no ha agregado comidas para comprar")

    if acciones == 3: #se ejecuta tercera accion (pagar)
        while True:
         total = 0
         items = 0
         for cantidad, precio in carrito_user: #recorremos el carrito del usuario para calcular el total
            total += cantidad*precio
            items += cantidad
            print(f"Cantidad de items: {items}, Costo total: {total} ")
            propina_sugeridad = total*0.1 #el 10% del total
            print(f"Propina sugerida 10%: $(propina_sugerida)")
            respuesta = input("Desea agregar propina? (s/n): ")
            if respuesta == "si":
                carrito_user.clear() #limpiamos el carrito
                print("Gracias por su compra")
            else:
                carrito_user.clear()
                ("Gracias por su compra")
            break
         

    if acciones == 4: #accion numero 4 quitar item de carrito
         while True:            
            item = input("Ingrese el item a quitar: ")
            quitar_item(carrito_user,item) #le agregamos la funcion quitar_item
            opcion = input("Desea quitar otro item? (s/n): ")
            if opcion == "si":
                continue
            if opcion == "no":  
                break
            print(carrito_user) #mostramos el carrito actualizado

            
    if acciones == 6: #accion numero 6 buscar item en carrito por ingredientes
        while True:
            ingrediente = input("Ingrese el ingrediente a buscar: ") 
            buscar_ingrediente(var,ingrediente) #le agregamos la lista de ingredientes
            opcion = input("Desea buscar otro ingrediente? (s/n): ")
            if opcion == "s":
                continue
            if opcion == "n":
                break
            
    if acciones == 9: #accion numero 9 modificar item del menu pidiendo contraseña
        for i, elementos in enumerate(var):
            print(f"{i+1} , {elementos}\n") #mostramos el menu
        contra = input("Ingrese la contraseña: ")
        if check_password(contra):
            id_producto= int(input("Ingrese el id del producto: ")) #ingresamos el id del producto a modificar 
            seleccion_producto = input("Ingrese que desea modificar (nombre,precio,kcal,ingredientes): ")
            producto = var[id_producto-1] #
            if seleccion_producto in producto.keys():
                modificacion = input("Ingrese nuevo dato: ")
                producto[seleccion_producto] = modificacion
        print(var) #mostramos el menu modificado

        
        
        
        
        #utilizo funcion (var) entregada en herramientas.py para mostrar el menu