def create_json_movie():
    title = input("Titulo: ")
    film_director = input("Director: ")
    release_date = input("Fecha de emisión (dd/mm/yyyy): ")
    genre = input("Género: ")
    writer = input("Escritor: ")
    cast = input("Reparto (Separado por ,): ")

    movie = {
        "title": title,
        "film_director": film_director,
        "release_date": release_date,
        "genre": genre,
        "writer": writer,
        "cast": cast
    }
    return movie


def create_json_movie_update():
    print("Menu de opciones")
    print("1. Modificar todo el documento")
    print("2. Moficar un elemento del documento")
    opcion = input("Ingrese una opcion: ")
    if opcion == "1":
        return create_json_movie()
    elif opcion == "2":
        indice = input("Ingrese el indice a buscar: ")
        valor = input("Ingrese el valor a sustituir: ")
        movie = {indice: valor}
        return movie


def select_opc_search():
    print("Opcion de busqueda")
    print("1. Buscar por titulo")
    print("2. Buscar por fecha de emisión")
    opcSearch = input("Ingrese una opción: ")
    if opcSearch == "1":
        title = input("Ingrese el titulo del registro a buscar: ")
        valor = {"title": title}
        return valor
    elif opcSearch == "2":
        release_date = input("Ingrese la fecha de emisión del registro a buscar (dd/mm/yyyy): ")
        valor = {"release_date": release_date}
        return valor
