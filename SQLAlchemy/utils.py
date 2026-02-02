from sqlalchemy.orm import Session
from src.SQLAlchemy.connection import engine, Base

def init_db():
    """Initialize database tables"""
    Base.metadata.create_all(bind=engine)

def drop_db():
    """Drop all database tables"""
    Base.metadata.drop_all(bind=engine)

def reset_db():
    """Reset database (drop and recreate all tables)"""
    drop_db()
    init_db()
