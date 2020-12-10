from pydantic import BaseModel
from datetime import date 
from typing import Dict

class DocumentInDB(BaseModel):
    id_document: int
    doc_name: str
    doc_send_date: date
    doc_active: bool
    id_module: int
    id_company: int

