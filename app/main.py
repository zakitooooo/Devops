from fastapi import FastAPI
from sqlalchemy import text
from database import engine, SessionLocal
from models import Item



app = FastAPI()

@app.get("/health")
def health():
    try :
        with engine.connect() as conn :
            conn.execute(text("SELECT 1"))
        db_status = "healthy"

    except :
        db_status = "unhealthy"
    return {"status": "healthy", "database": db_status}     
@app.post("/items")
def create_Item(name:str , description: str | None = None) :
    db = SessionLocal()
    item = Item(name=name,  description=description)
    db.add(item)
    db.commit()
    db.refresh(item)
    db.close()
    return {"id": item.id, "name": item.name, "description": item.description}

@app.get("/items")
def get_items():
    db = SessionLocal()
    items = db.query(Item).all()
    db.close()
    return items
@app.get("/items/{id}")
def get_item(item_id:int) :
    db = SessionLocal()
    item = db.query(Item).filter(Item.id == item_id).first()
    db.close()
    return item
@app.delete("/items/{id}")
def delete_item(item_id=int):
    db = SessionLocal()
    item = db.query(Item).filter(Item.id == item_id).first()
    db.delete(item)
    db.commit()
    db.close()
    return {"message" : "Item deleted"}


