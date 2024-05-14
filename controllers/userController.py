import services.database as db
import models.user as user

def create(usuario : user):
    
    format_user = {
        "nome": usuario.name,
        "cpf": usuario.cpf,
        "senha": usuario.password
    }

    db.user_collection.insert_one(format_user)

def read(cpf : str):
   
    return db.user_collection.find_one({"cpf": cpf})