from sqlalchemy import String,DateTime,Integer,Column
from sqlalchemy.sql import func
from uuid import uuid4
from database import Base
import uuid


class Items(Base):
    __tablename__ = 'trunking_calling_setting'

    id = Column(String, primary_key=True, index=True, default=str(uuid.uuid4()))
    call_number = Column(Integer)
    alias = Column(String)
    location = Column(String)
    call_num_status = Column(String)
    calling_attribute = Column(String)
    outbound_time = Column(String)
    trunking_status = Column(String)
    concurrency = Column(Integer)
    area_code = Column(Integer)
    comment = Column(String)
    created_time = Column(DateTime(timezone=True), server_default=func.now())
    updated_time = Column(DateTime(timezone=True), onupdate=func.now())


    