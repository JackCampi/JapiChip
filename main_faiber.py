from db.expiration_db import ExpirationInDB, insert_expiration, search_expiration, update_expiration_db
from db.process_db import search_doc_id, put_expiration_id, delete_expiration_id
from models.expiration_model import ExpirationCreateIn, ExpirationDeleteIn, ExpirationGetIn, ExpirationGetOut, ExpirationUpdateIn

import datetime
from fastapi import FastAPI
from fastapi import HTTPException

api = FastAPI()


@api.put("/expiration")
async def put_expiration(expiration_create_in: ExpirationCreateIn):
    periodicity_type = expiration_create_in.exp_periodicity_type
    if periodicity_type == "day" or periodicity_type == "week" or periodicity_type == "month" or periodicity_type == "year":
        process = search_doc_id(expiration_create_in.doc_id)
        if process == None:
            return {"document": "No exist"}

        elif process.expiration_id == 0:
            expiration_in_db = ExpirationInDB(
                **expiration_create_in.dict(), exp_id=0)
            expiration = insert_expiration(expiration_in_db)
            put_expiration_id(expiration.exp_id, expiration_create_in.doc_id)
            return {"process:": True}

        else:
            return {"Expiration": "Exist, no created"}

    else:
        return {"periodicity_type": "day, week, month, year"}


@api.delete("/expiration")
async def delete_expiration(expiration_delete_in: ExpirationDeleteIn):
    doc_id = expiration_delete_in.doc_id
    process = search_doc_id(doc_id)
    if process == None:
        return {"result": "No exist document or expiration"}

    elif process.expiration_id == 0:
        return {"result": "Expiration not exist"}

    else:
        exp_id = process.doc_id
        delete_expiration_id(doc_id)
        delete_expiration(exp_id)
        return {"delete_expiration": "true"}


@api.post("/expiration")
async def get_expiration(expiration_get_in: ExpirationGetIn):
    exp_id = expiration_get_in.exp_id
    expiration = search_expiration(exp_id)
    if expiration == None:
        return {"expiration": "No exist"}
    expiration = ExpirationGetOut(**expiration.dict())
    return expiration


@api.post("/expiration/update")
async def update_expiration(expiration_update_in: ExpirationUpdateIn):
    if update_expiration_db(expiration_update_in):
        return {"expiration": "update"}
    return {"expiration": "No update"}
