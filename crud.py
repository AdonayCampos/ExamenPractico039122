from conection import collection


def show_movie(opc_search= None):
    if opc_search is None:
        documents = collection.find()
        for document in documents:
            print(document)
    else:
        documents = collection.find(opc_search)
        for document in documents:
            print(document)


def create_movie(movie):
    result = collection.insert_one(movie)
    print(result.inserted_id)


def update_movie(id, json_update):
    query = {"_id": id}
    new_values = {"$set": json_update}
    result = collection.update_one(query, new_values)
    print(result.modified_count)

def delete_movie(title):
    query = {"title": title}
    result = collection.delete_one(query)
    print(result.deleted_count)