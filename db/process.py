from pydantic import BaseModel

class ProcessInDB(BaseModel):
    id_user: int
    id_document: int
    id_expiration: int
    proc_ready: bool
