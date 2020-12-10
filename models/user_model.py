from pydantic import BaseModel

class UserIn(BaseModel):
    documentnumberuser: int
    firstnameuser: str
    lastnameuser: str
    emailuser: str
    passworduser: str
    typeofuser: str
    documentnumbercompany : int

