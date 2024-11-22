from pydantic import BaseModel

class UserBase(BaseModel):
    nome : str
    email : str
    senha : str

class UserLogin(BaseModel):
    email : str
    senha : str