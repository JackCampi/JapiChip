from pydantic import BaseModel

class ProcessInDB(BaseModel):
    user_email: str
    doc_id: int
    expiration_id: int
    proc_ready: bool
