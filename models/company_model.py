from pydantic import BaseModel

class Company(BaseModel):
    documenttype = str
    documentnumber = int
    persontype = str
    personname = str
    address = str
    country = str
    city = str
    phonenumber = str
    email = str

"""
class Company:
    def __init__(self, documenttype, documentnumber, persontype, personname, address, country, city, phonenumber, email):
        self.dt = documenttype
        self.dn = documentnumber
        self.pt = persontype
        self.pn = personname
        self.a = address
        self.co = country
        self.ci = city
        self.pho = phonenumber
        self.e = email
"""
        
