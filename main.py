from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import MetaData
from . import crud, models, schemas
from database import SessionLocal, Engine, Base

models.Base.metadata.create_all(bind=Engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()    

app = FastAPI()        

origins = ["http://localhost:3000", "http://127.0.0.1"]
app.add_middleware(
    CORSMiddleware,
    allow_origis = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.get('/items/{item_id}',response_model=schemas.Items_schemas,status_code=status.HTTP_200_OK)
def read_item(item_id:int, db:Session=Depends(get_db)):
    db_item = crud.get_item(db, items_id=item_id)
    return db_item

@app.get('/items',response_model=List[schemas.Items_schemas],status_code=status.HTTP_200_OK)
def read_all_items(skip: int=0, limit: int=10, db: Session=Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

@app.post('/items',response_model=schemas.Items_cteate, status_code=status.HTTP_201_CREATED)
def create_an_item(item: schemas.Items_cteate, db: Session=Depends(get_db)):
    db_item = crud.create_item(db, item=item)
    return db_item

@app.put('/items',response_model=schemas.Items_update,status_code=status.HTTP_200_OK)
def update_an_item(item: schemas.Items_update, db: Session=Depends(get_db)):
    db_item = crud.update_item(db, item=item)
    return db_item

@app.delete('/items/{item_id}', response_model=schemas.Items_schemas, status_code=status.HTTP_200_OK)
def delete_an_item(item_id:int, db: Session=Depends(get_db)):
    db_item = crud.delete_item(db, items_id=item_id)
    return db_item
