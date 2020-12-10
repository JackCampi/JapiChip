from pydantic import BaseModel

class Submodul(BaseModel):
    submodulname = str
    companyid = int
    moduloid = int

"""class Submodulo(Modulo):
    def __init__(self, submoduloname, companyid, moduloid):
        self.name = submoduloname
        self.company = companyid
        self.modulo = moduloid"""