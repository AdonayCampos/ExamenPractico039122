from function_basic import *
from crud import *

while True:
    print("Menu de opciones")
    print("1. Ver todas las peliculas")
    print("2. Buscar una pelicula")
    print("3. Agregar una pelicula")
    print("4. Modificar una pelicula")
    print("5. Eliminar una pelicula")
    print("6. Salir del sistema")

    opcion = input("Ingrese una opcion: ")
    if opcion == "1":
        show_movie()
    elif opcion == "2":
        valor = select_opc_search()
        show_movie(valor)
    elif opcion == "3":
        movie = create_json_movie()
        create_movie(movie)
    elif opcion == "4":
        id = int(input("Ingrese el id del registro a modificar: "))
        movie = create_json_movie_update()
        update_movie(id, movie)
    elif opcion == "5":
        title = input("Ingrese el titulo de la pelicula a eliminar: ")
        delete_movie(title)
    elif opcion == "6":
        break
