from typing import Dict
from pydantic import BaseModel


class CompanyInDB(BaseModel):
    comp_id: int
    comp_name: str


database_company = Dict[int, CompanyInDB]

database_company = {
    1: CompanyInDB(**{"comp_id": 1,
                      "comp_name": "Contadoras Unaleñas"}),

    2: CompanyInDB(**{"comp_id": 2,
                      "comp_name": "Emprendedores Unaleños"}),
}


def get_empresa(comp_id: int):
    if comp_id in database_company.keys():
        return database_company[comp_id]
    else:
        return None


def update_empresa(company_in_db: CompanyInDB):
    database_company[company_in_db.comp_id] = company_in_db
    return company_in_db
