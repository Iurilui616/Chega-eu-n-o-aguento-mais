# ================= IMPORTS =================
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import (
    create_engine, Column, Integer, String, Date, DateTime,
    Text, Boolean, ForeignKey, Enum
)
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime
import enum

# ================= CONFIG =================
DATABASE_URL = "postgresql+psycopg2://user:password@db:5432/achados"
SECRET_KEY = "test"
ALGORITHM = "HS256"

# ================= DATABASE =================
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# ================= ENUM =================
class TipoOcorrencia(enum.Enum):
    perdido = "perdido"
    encontrado = "encontrado"

# ================= MODELS (DER) =================
class Usuario(Base):
    __tablename__ = "usuario"
    id_usuario = Column(Integer, primary_key=True)
    nome = Column(String)
    email = Column(String, unique=True)
    senha = Column(String)
    telefone = Column(String)
    tipo_usuario = Column(String)
    data_cadastro = Column(DateTime)

class Objeto(Base):
    __tablename__ = "objeto"
    id_objeto = Column(Integer, primary_key=True)
    nome_objeto = Column(String)
    descricao = Column(Text)
    categoria = Column(String)
    cor = Column(String)
    data_ocorrencia = Column(Date)
    status = Column(String)
    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario"))

class Local(Base):
    __tablename__ = "local"
    id_local = Column(Integer, primary_key=True)
    nome_local = Column(String)
    descricao = Column(Text)
    cidade = Column(String)
    estado = Column(String)

class Ocorrencia(Base):
    __tablename__ = "ocorrencia"
    id_ocorrencia = Column(Integer, primary_key=True)
    tipo = Column(Enum(TipoOcorrencia))
    data_registro = Column(DateTime)
    observacoes = Column(Text)
    id_objeto = Column(Integer, ForeignKey("objeto.id_objeto"))
    id_local = Column(Integer, ForeignKey("local.id_local"))

class Mensagem(Base):
    __tablename__ = "mensagem"
    id_mensagem = Column(Integer, primary_key=True)
    conteudo = Column(Text)
    data_envio = Column(DateTime)
    id_remetente = Column(Integer, ForeignKey("usuario.id_usuario"))
    id_destinatario = Column(Integer, ForeignKey("usuario.id_usuario"))
    id_objeto = Column(Integer, ForeignKey("objeto.id_objeto"))

class Imagem(Base):
    __tablename__ = "imagem"
    id_imagem = Column(Integer, primary_key=True)
    caminho_arquivo = Column(String)
    id_objeto = Column(Integer, ForeignKey("objeto.id_objeto"))

class Devolucao(Base):
    __tablename__ = "devolucao"
    id_devolucao = Column(Integer, primary_key=True)
    data_devolucao = Column(Date)
    status_confirmacao = Column(Boolean)
    id_objeto = Column(Integer, ForeignKey("objeto.id_objeto"))
    id_usuario_dono = Column(Integer, ForeignKey("usuario.id_usuario"))
    id_usuario_encontrou = Column(Integer, ForeignKey("usuario.id_usuario"))

Base.metadata.create_all(engine)

# ================= JWT =================
pwd_context = CryptContext(schemes=["bcrypt"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def criar_token(dados: dict):
    return jwt.encode(dados, SECRET_KEY, algorithm=ALGORITHM)

def usuario_logado(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload["sub"]
    except JWTError as e:
        print(f"JWT Error: {e}")
        raise HTTPException(status_code=401, detail="Token inválido")

# ================= APP =================
app = FastAPI(title="API Achados e Perdidos")

# ================= ROTAS =================
@app.post("/login")
def login(email: str, senha: str):
    db = SessionLocal()
    user = db.query(Usuario).filter(Usuario.email == email).first()
    if not user or not pwd_context.verify(senha, user.senha):
        raise HTTPException(status_code=401)
    return {"access_token": criar_token({"sub": str(user.id_usuario)})}

@app.get("/protegido")
def rota_protegida(user_id=Depends(usuario_logado)):
    return {"usuario_id": user_id}
