"""
Puede escribir aqui las funciones del codigo
Se importaran de forma automatica al 'main.py'
"""
# ------ NO BORRAR -----
def test () -> None:
    """
        Funcion para probar el archivo
    """
    import herramientas
    menu = herramientas.load_items('menu.csv')
    print(menu)

# esto es para que test solo corra si es ejecutado directamente
if __name__ == '__main__':
    test()
# ------ NO BORRAR -----

#Escribir Funciones desde aqui hacia abajo ------------
carrito_user = []
#ejemplo de funcion
#funcion ver_menu que recibe una lista de diccionarios y muestra el menu
def ver_menu(mostrar_menu):
    for productos in mostrar_menu: 
        print(f"{productos ['nombre']} ---> Precio = {productos['precio']}") #recorremos el menu y mostramos el nombre y el precio desde el diccionario
    while True:
        opcion = input("Desea agregar alguna comida a su carrito de compras? (s/n): ")
        if opcion == "si":
            item = input("Seleccione alguna comida que desee agregar al carrito: ")
            for elemento in mostrar_menu:
                if item in elemento.values():
                    carrito_user.append(elemento)
        if opcion == "no":
            break
        

def quitar_item(carrito, items):               #funcion para quitar items del carrito #recibe como parametros el carrito y el item a quitar                             
         for producto in carrito:
          if producto["nombre"] == items:
            carrito.remove(producto)
            print(f"Se ha quitado {items} del carrito.")
            break
         else:
          print(f"{items} no se encuentra en el carrito.")




def buscar_ingrediente(lista_carrito,ingredientes): #funcion para modificar el menu con contraseña
    for producto in lista_carrito:
        ingredientes = producto["ingredientes"]
        if ingredientes in ingredientes:
            print(producto)








