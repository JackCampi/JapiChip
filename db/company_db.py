from pydantic import BaseModel

class CompanyInDB(BaseModel):
    documentnumbercompany : int
    documenttypecompany : str
    personnamecompany : str
    persontypecompany : str
    addresscompany : str
    countrycompany : str
    citycompany : str
    phonenumbercpmpany : str
    emailcompany : str

database_companies = Dict[str, CompanyInDB]

database_companies = {
    "900354115": CompanyInDB((**{"documentnumbercompany":900354115,
                            "documenttypecompany":"NIT",
                            "personnamecompany":"La Comercializadora",
                            "persontypecompany":"Persona Juridica",
                            "addresscompany": "Cr 22 a 190",
                            "countrycompany": "Colombia",
                            "citycompany": "Bogota",
                            "phonenumbercompany": "3206112020",
                            "emailcompany": "lacomercializadora@lacomercializadora.com"}),
}

def get_company(documentnumbercompany: int):
    if documentnumbercompany in database_companies.keys():
        return database_companies[personnamecompany]
    else:
        return None