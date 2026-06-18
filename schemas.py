from pydantic import BaseModel, ConfigDict

class ItemsBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    call_number: int
    alias: str
    location: str
    call_num_status: str
    calling_attribute: str
    outbound_time: str
    trunking_status: str
    concurrency: int
    area_code: int
    comment: str


class Items_update(ItemsBase):
    pass
    
class Items_create(ItemsBase):
    id: str

class Items(ItemsBase):
    id: str
