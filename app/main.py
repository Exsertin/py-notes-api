from fastapi import FastAPI
from app.routes import users, notes
from app.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Notes API")

@app.get("/")
def read_root():
    return {"message": "Welcome to Notes API"}

app.include_router(users.router)
app.include_router(notes.router)
