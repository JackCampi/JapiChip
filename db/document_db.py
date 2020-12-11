from pydantic import BaseModel
from datetime import date 
from typing import Dict

class DocumentInDB(BaseModel):
    doc_id: int = 0
    doc_name: str
    doc_send_date: str
    doc_active: bool
    mod_id: int

database_documents = []


def insert_doc(document_in_db: DocumentInDB):
    document_in_db.doc_id = len(database_documents)
    database_documents.append(document_in_db)
    return document_in_db

def get_doc(doc_id : int):
    return database_documents[doc_id]