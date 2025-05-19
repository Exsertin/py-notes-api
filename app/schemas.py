from pydantic import BaseModel

class NoteBase(BaseModel):
    title: str
    content: str

class NoteCreate(NoteBase):
    pass

class Note(NoteBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    username: str
    password: str

class User(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True
