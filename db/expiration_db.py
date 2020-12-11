from pydantic import BaseModel
from datetime import date

class ExpirationInDB(BaseModel):
    exp_id: int
    exp_date: date
    exp_periodicity: int
    exp_periodicity_type: str

database_expiration = [ExpirationInDB(**{
    'id_exp': 0,
    'exp_date': date.today(),
    'exp_periodicity': 0,
    'exp_periodicity_type': None
})]



def insert_expiration(expiration_in_db: ExpirationInDB):
    expiration_in_db.id_exp = len(database_expiration)
    database_expiration.append(expiration_in_db)
    return expiration_in_db
