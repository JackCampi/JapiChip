from pydantic import BaseModel

class Company(BaseModel):
    documentnumbercompany : int
    documenttypecompany : str
    personnamecompany : str
    persontypecompany : str
    addresscompany : str
    countrycompany : str
    citycompany : str
    phonenumbercpmpany : str
    emailcompany : str

        
