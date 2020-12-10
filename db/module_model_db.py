from pydantic import BaseModel
from datetime import date 
from typing import Dict

class ModulInDB(BaseModel):
    namemodule : str
    documentnumbercompany : int
    fathermodule : int

database_module = Dict[str, ModulInDB]

"""database_module = {
    "1": ModulInDB(**{"username":"camilo24",
                            "password":"root",
                            "balance":12000}),

    "andres18": ModulInDB(**{"username":"andres18",
                            "password":"hola",
                            "balance":34000}),
}"""

"""def get_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    else:
        return None

def update_user(user_in_db: UserInDB):
    database_users[user_in_db.username] = user_in_db
    return user_in_db"""