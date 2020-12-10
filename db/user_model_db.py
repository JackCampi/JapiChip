from pydantic import BaseModel
from datetime import date 
from typing import Dict

class UserInDB(BaseModel):
    documentnumberuser: int
    firstnameuser: str
    lastnameuser: str
    emailuser: str
    passworduser: str
    typeofuser: str
    documentnumbercompany : int

database_users = Dict[str, UserInDB]

database_users = {
    "ricardo": UserInDB(**{"documentnumberuser":1053820000,
                            "firstnameuser":"Ricardo",
                            "lastnameuser": "Jaramillo",
                            "emailuser": "administrador@lacomercializadora.com",
                            "passworduser": "321",
                            "typeofuser" : "administrador",
                            "documentnumbercompany": 900354115
                            }),

    "rosa": UserInDB(**{"documentnumberuser":75202000,
                            "firstnameuser":"Rosa",
                            "lastnameuser": "Gonzalez",
                            "emailuser": "asistente@lacomercializadora.com",
                            "passworduser": "321",
                            "typeofuser" : "asistente",
                            "documentnumbercompany": 900354115
                            }),
}

def get_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    else:
        return None

def update_user(user_in_db: UserInDB):
    database_users[user_in_db.username] = user_in_db
    return user_in_db