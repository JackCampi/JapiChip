from typing import Dict
from pydantic import BaseModel


class UserInBD(BaseModel):
    user_id: int
    user_name: str
    user_lastname: str
    user_email: str
    user_password: str
    user_rol: str
    user_comp_id: int


database_user = Dict[int, UserInBD]

database_user = {
    1: UserInBD(**{"user_id": 1,
                   "user_name": "Perez",
                   "user_lastname": "Cardona",
                   "user_email": "perez-cardona@gmail.com",
                   "user_password": "12345",
                   "user_rol": "Lider",
                   "user_comp_id": 1}),

    2: UserInBD(**{"user_id": 2,
                   "user_name": "Camilo",
                   "user_lastname": "Ronaldo",
                   "user_email": "camilo-ronaldo@gmail.com",
                   "user_password": "12345",
                   "user_rol": "secretario",
                   "user_comp_id": 1}),

    3: UserInBD(**{"user_id": 3,
                   "user_name": "Edwin",
                   "user_lastname": "Vinasco",
                   "user_email": "edwin-vinasco@gmail.com",
                   "user_password": "12345",
                   "user_rol": "Lider",
                   "user_comp_id": 2}),

    4: UserInBD(**{"user_id": 4,
                   "user_name": "Andres",
                   "user_lastname": "Camacho",
                   "user_email": "andrea-camacho@gmail.com",
                   "user_password": "12345",
                   "user_rol": "secretario",
                   "user_comp_id": 2})
}
