from pydantic import BaseModel

class ModuleIn(BaseModel):
    mod_id : int
    mod_name : str
    comp_id : int
    mod_parent_id : int