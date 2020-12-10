from pydantic import BaseModel

class Module(BaseModel):
    namemodule : str
    documentnumbercompany : int
    fathermodule : int