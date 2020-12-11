
from db.user_db import get_user
from db.module_db import insert_module2, exist_module, ModuleInDB
from db.company_db import insert_company

from models.user_model import UserIn
from models.module_model import ModuleIn
from models.company_model import CompanyIn

from fastapi import FastAPI
from fastapi import HTTPException

api = FastAPI()

@api.post("/user/auth/")
async def auth_user(user : UserIn):
    user_in_db = get_user(user.user_email)
    if user_in_db == None:
        raise HTTPException(status_code=404,
                            detail="El usuario no existe")
    if user.user_password == user_in_db.user_password:
        return {"Authentication" : True}
    return {"Authentication" : False}

@api.post("/company/modules/create/")
async def create_module(module : ModuleIn):
    if exist_module(module.mod_parent_id):
        module_in_db = ModuleInDB(**{"mod_name": module.mod_name,
                                    "comp_id": module.comp_id,
                                    "mod_parent_id": module.mod_parent_id}),
        try:
            insert_module2(module_in_db)
            return {"Created" : True}
        except Exception as e:
            
            raise HTTPException(status_code=404, #Status code isn't 
                            detail=str(e))
    else:
        raise HTTPException(status_code=404,
                            detail="El módulo padre no existe")

@api.post("/new_company/")
async def create_company(company : CompanyIn):
    try:
        insert_company(company)
        return {"Created" : True}
    except Exception as e:
        raise HTTPException(status_code=400,
                            detail= str(e))
