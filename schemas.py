from pydantic import BaseModel

class ItemsBase(BaseModel):
    call_number: int
    alias: str
    location: str
    call_num_status: str
    calling_attribute: str
    outbound_duration: str
    trunking_stattus: str
    concurrency: int
    area_code: int
    comment: str

class Items_cteate(ItemsBase):
    pass

class Items_update(ItemsBase):
    pass
    
class Items_schemas(ItemsBase):
    id: int

    class Config:
        orm_mode = True