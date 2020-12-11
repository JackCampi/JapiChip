from pydantic import BaseModel
from datetime import date 
from typing import Dict

class DocumentInDB(BaseModel):
    doc_id: int
    doc_name: str
    doc_send_date: date
    doc_active: bool
    mod_id: int
    comp_id: int
