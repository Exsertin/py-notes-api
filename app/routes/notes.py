from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, models, database, auth
from typing import List

router = APIRouter(prefix="/notes", tags=["notes"])

@router.post("/", response_model=schemas.Note)
def create_note(note: schemas.NoteCreate, db: Session = Depends(database.SessionLocal), current_user: models.User = Depends(auth.get_current_user)):
    db_note = models.Note(**note.dict(), owner_id=current_user.id)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)

    return db_note

@router.get("/", response_model=List[schemas.Note])
def get_notes(db: Session = Depends(database.SessionLocal), current_user: models.User = Depends(auth.get_current_user)):
    return db.query(models.Note).filter(models.Note.owner_id == current_user.id).all()
