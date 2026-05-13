from pymongo import MongoClient #Para utilizar este función se debe instalar "python -m pip install pymongo"

#Se crea la conexion a la base de datos
def conexionMongo():
    try:
        conexion = MongoClient("mongodb://localhost:27017/") #SE PONE LOS DATOS DEL CLIENTE QUE EN ESTE CASO ES 
        conexion.server_info()
        db = conexion.EVALUACION3 #ASIGNAMOS A "db" LA CONEXION DE LA BASE EVALUACION3
        collection = db.Personas #ASIGNAMOS A "collection" "db.Personas"
        print("Conexion exitosa")
    except:
        print("Error al conectar a Mongo")
    return(collection)

collection = conexionMongo()

def personaInsert(rut, edad, sexo): #FUNCION PARA INSERTAR DOCUMENTOS EN LA BASE
    rutExiste = collection.find_one({"RUT": rut}) #SE COMPRUEBA QUE RUT NO ESTÉ REGISTRADO EN LA BD
    if rutExiste:
        print("\nEl documento a ingresar ya existe\n")
    else:
        collection.insert_one( #SE INSERTA LOS DATOS EN LA BASE
            {
                "RUT": rut,
                "EDAD": edad,
                "SEXO": sexo
            }
        )
        print("\nEl documento fue guardado de manera correcta\n")


def personaFind(rut): #FUNCION PARA BUSCAR DOCUMENTOS EN LA BASE
    persona = collection.find_one({"RUT": rut}, {"_id": 0})

    if persona:
        print("\n\nDocumento encontrado: ")
        print(f"\n\tRUT: {persona["RUT"]}\n\tEDAD: {persona["EDAD"]}\n\tSEXO: {persona["SEXO"]}\n")
    else: 
        print("\nEl documento a buscar no existe\n")

def personaUpdate(rut, edad, sexo): #FUNCION PARA ACTUALIZAR DOCUMENTOS EN LA BASE
    rutExiste = collection.find_one({"RUT": rut})

    if rutExiste: 
        collection.update_one({ #SE INSERTA DATOS A ACTUALIZAR EN LA BASE
            "RUT": rut 
        },{
            "$set": {
                "EDAD": edad,
                "SEXO": sexo
            }
        })
        print("\nEl documento fue actualizado de manera correcta\n")

        persona = collection.find_one({"RUT": rut}, {"_id": 0}) #SE MUESTRA DOCUMENTO ACTUALIZADO EN LA BASE
        print("\nDatos actualizados: ")
        print(f"\n\tRUT: {persona["RUT"]}\n\tEDAD: {persona["EDAD"]}\n\tSEXO: {persona["SEXO"]}\n")
    else:
        print("\nEl documento a actualizar no existe\n")

def personaDelete(rut): #FUNCION PARA ELIMINAR DOCUMENTOS EN LA BASE
    rutExiste = collection.find_one({"RUT": rut})

    if rutExiste:
        persona = collection.find_one({"RUT": rut}, {"_id": 0}) #SE MUESTRA DOCUMENTO A ELIMINAR EN LA BASE
        print("\nDatos a Eliminar: ")
        print(f"\n\tRUT: {persona["RUT"]}\n\tEDAD: {persona["EDAD"]}\n\tSEXO: {persona["SEXO"]}\n")

        collection.delete_one({"RUT": rut}) #SE ELIMINA EL DOCUMENTO EN LA BASE
        print("\nEl documento fue eliminado de manera correcta\n")
    else:
        print("\nEl documento a eliminar no existe\n")

#Insertar Documentos:
'''
personaInsert("1-9", 5, "Masculino")
personaInsert("2-8", 10, "Femenino")
personaInsert("3-7", 15, "Masculino")
personaInsert("4-6", 20, "Femenino")
personaInsert("5-5", 25, "Femenino")
personaInsert("6-4", 30, "Masculino") '''

#Buscar Documentos:

'''
personaFind("3-7") ''' 

#Actualizar Documentos: Documentos
'''
personaUpdate("2-8", 16, "Masculino")
personaUpdate("4-6", 26, "Femenino") '''

#Eliminar Documentos
'''
personaDelete("1-9")
personaDelete("2-8")
personaDelete("3-7") '''