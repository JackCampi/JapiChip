from typing import Dict
from pydantic import BaseModel


class ModuleInDB(BaseModel):
    mod_int: int
    mod_name: str
    mod_comp_id: int
    mod_father_id: int


database_modules = Dict[int, ModuleInDB]

database_modules = {
    0: ModuleInDB(**{"mod_int": 0,
                     "mod_name": "Modulo Raiz",
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
}
