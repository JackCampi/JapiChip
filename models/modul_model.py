from pydantic import BaseModel

class Modul(BaseModel):
    modulname = str
    companyid = int

"""class Modulo:
    def __init__(self, moduloname, companyid):
        self.name = moduloname
        self.company = companyid
"""