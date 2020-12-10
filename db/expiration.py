from pydantic import BaseModel
from datetime import date

class ExpirationInDB(BaseModel):
    id_exp: int
    exp_date: date
    exp_periodicity: int
    exp_periodiciyy_type: str

database_expiration = [ExpirationInDB(**{
    'id_exp': 0,
    'exp_date': date.today(),
    'exp_periodicity': 0,
    'exp_periodicity_type': None
})]
generator = {'id': 1}

database_expiration.append(0)

def create_expiration(expiration_in_db: ExpirationInDB):
    generator['id'] = generator['id'] + 1
    expiration_in_db.id_exp = generator['id']
    database_expiration.append(expiration_in_db)
    return expiration_in_db
