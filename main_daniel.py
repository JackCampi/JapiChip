from fastapi import FastAPI, File, UploadFile
from fastapi import HTTPException

from models.document_model import DocumentIn
from db.user_db import get_user
from db.document_db import DocumentInDB
from db.document_db import insert_doc, get_doc
from db.process_db import ProcessInDB
from db.process_db import create_process, get_user_docs_id


api = FastAPI()

'''@api.post('/upload_doc/')
async def upload_file(doc_info: DocumentIn, file: UploadFile = File(...)):
    print(type(file))
    return {
        "filename": file.filename,
        'doc_name': doc_info.doc_name
        }'''

@api.post('/docs/upload/')
async def update_file_info(doc_info: DocumentIn):
    document = DocumentInDB(**{
        'doc_name': doc_info.doc_name,
        'doc_send_date' : doc_info.doc_send_date,
        'doc_active' : doc_info.doc_active,
        'mod_id': doc_info.mod_id
    })
    document = insert_doc(document)
    for user_email in doc_info.user_emails:
        user_in_db = get_user(user_email)
        if user_in_db == None:
            raise HTTPException(status_code=404,
                                detail=f"El usuario {user_email} no existe")
        
        process = ProcessInDB(**{
            'user_email': user_email,
            'doc_id': document.doc_id,
            'expiration_id':0,
            'proc_ready': True
        })

        create_process(process)
    return {'Document Inserted': True}

@api.get('/docs/{user_email}')
async def get_docs_from_user(user_email: str):
    user_in_db = get_user(user_email)
    if user_in_db == None:
        raise HTTPException(status_code=404,
                            detail=f"El usuario {user_email} no existe")
    
    docs_id = get_user_docs_id(user_email)
    docs = []
    for doc_id in docs_id:
        docs.append(get_doc(doc_id))
    return {
        'item_found': len(docs),
        'items': docs
    }