from pydantic import BaseModel
from datetime import date 
from typing import Dict

class ModulInDB(BaseModel):
    namemodule : str
    documentnumbercompany : int
    fathermodule : int

database_module = Dict[str, ModulInDB]

"""
database_modules = {
    0: ModuleInDB(**{"mod_name": "Modulo Raiz",
                     "mod_comp_id": 0,
                     "mod_father_id": 0}),

    1: ModuleInDB(**{"mod_int": 1,
                     "mod_name": "Recursos Humanos",
                     "mod_comp_id": 1,
                     "mod_father_id": 0}),

    2: ModuleInDB(**{"mod_int": 2,
                     "mod_name": "Derecho Laboral",
                     "mod_comp_id": 1,
                     "mod_father_id": 1}),

    3: ModuleInDB(**{"mod_int": 3,
                     "mod_name": "Recursos Humanos",
                     "mod_comp_id": 2,
                     "mod_father_id": 0}),

    4: ModuleInDB(**{"mod_int": 4,
                     "mod_name": "Derecho Laboral",
                     "mod_comp_id": 2,
                     "mod_father_id": 3}),
}"""

"""def get_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    else:
        return None

def update_user(user_in_db: UserInDB):
    database_users[user_in_db.username] = user_in_db
    return user_in_db"""