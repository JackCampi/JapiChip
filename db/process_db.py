from pydantic import BaseModel

class ProcessInDB(BaseModel):
    proc_id: int = 0
    user_email: str
    doc_id: int
    expiration_id: int
    proc_ready: bool

database_process = []


def create_process(process_in_db: ProcessInDB):
    ProcessInDB.proc_id = len(database_process)
    database_process.append(process_in_db)
    return process_in_db

def  get_user_docs_id(user_email):
    docs = []
    for process in database_process:
        if  process.user_email == user_email:
            docs.append(process.doc_id)
    return docs