from fastapi import FastAPI, HTTPException, Header
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String
import jwt
from datetime import datetime, timedelta
import bcrypt
import requests
import os
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

class UserBase(BaseModel):
    nome : str
    email : str
    senha : str

class UserLogin(BaseModel):
    email : str
    senha : str

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    nome = Column(String(100))
    email = Column(String(100))
    senha = Column(String)

app = FastAPI()

SECRET_KEY = os.getenv("SECRET_KEY", "secret_key")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# DATABASE_URL = "sqlite:///./test.db"
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://usuario:senha@db/banco")
engine = create_engine(DATABASE_URL, echo=False)
session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)

headers_consultar = {"Accept-Encoding": "gzip, deflate"}

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@app.get("/")
async def root():
    return {"message": "Página inicial"}

@app.post("/registrar")
async def registrar(user: UserBase):
    db = session()

    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        db.close()
        raise HTTPException(status_code=409, detail="Email já existe!")
    
    senha_hash = bcrypt.hashpw(user.senha.encode('utf-8'), bcrypt.gensalt())
    
    new_user = User(nome=user.nome, email=user.email, senha=senha_hash.decode('utf-8'))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    db.close()

    token_data = {"email": user.email}
    jwt_token = create_access_token(token_data)

    return {"jwt": jwt_token}

@app.post("/login")
async def login(user: UserLogin):
    db = session()

    existing_user = db.query(User).filter(User.email == user.email).first()
    if not existing_user:
        db.close()
        raise HTTPException(status_code=404, detail="Usuário não encontrado!")
    
    if not bcrypt.checkpw(user.senha.encode('utf-8'), existing_user.senha.encode('utf-8')):
        db.close()
        raise HTTPException(status_code=401, detail="Senha incorreta!")
    
    db.close()

    token_data = {"email": user.email}
    jwt_token = create_access_token(token_data)

    return {"jwt": jwt_token}

@app.get("/dados")
async def dados():
    db = session()
    users = db.query(User).all()
    db.close()
    return users

@app.get("/consultar")
async def consultar(token: str = Header(None)):
    if not token:
        raise HTTPException(status_code=401, detail="Token não fornecido!")
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("email")

        if not email:
            raise HTTPException(status_code=403, detail="Token inválido!")
        
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=403, detail="Token expirado!")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=403, detail="Token inválido!")
    
    response = requests.get("https://api.coincap.io/v2/assets", headers = headers_consultar)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Erro ao chamar a API externa")
    
    api_data = response.json()
    filtered_data = api_data["data"][:10]
    
    return filtered_data