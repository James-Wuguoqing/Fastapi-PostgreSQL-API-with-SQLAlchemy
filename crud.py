from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import models, schemas 

def get_item(db:Session, items_id:int):
    db_item = db.query(models.Items).filter(models.Items.id == items_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="db_item not found")
    return db_item

def get_items(db:Session, skip: int=0, limit: int=10):
    db_item = db.query(models.Items).offset(skip).limit(limit).all()
    return db_item

def create_item(db:Session, item:schemas.Items_cteate):
    db_item = models.Items(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_item(db:Session, item: schemas.Items_update):
    db_item = models.Items(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item 

def delete_item(db: Session, items_id: int):
    db_item = get_item(db, items_id)
    db.delete(db_item)
    db.commit()
    message = {"message": "A db_item recored is deleted successfully"}
    return message