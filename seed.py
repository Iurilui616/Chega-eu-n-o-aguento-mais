from datetime import datetime
from app import SessionLocal, Usuario
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"])

db = SessionLocal()

if not db.query(Usuario).first():
    user = Usuario(
        nome="Admin",
        email="admin@email.com",
        senha=pwd_context.hash("123"),
        telefone="0000-0000",
        tipo_usuario="admin",
        data_cadastro=datetime.now()
    )
    db.add(user)
    db.commit()
    print("Seed criado")
else:
    print("Seed já existe")
