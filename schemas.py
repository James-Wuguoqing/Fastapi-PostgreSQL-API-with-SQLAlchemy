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

    class config:
        orm_mode = True


class Items_update(ItemsBase):
    pass
    
class Items_create(ItemsBase):
    id: str

    class Config:
        orm_mode = True

class Items(ItemsBase):
    id: str

    class Config:
        orm_mode = True