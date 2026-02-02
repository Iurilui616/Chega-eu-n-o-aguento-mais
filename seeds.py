from sqlalchemy.orm import Session
from faker import Faker
from src.database.connection import get_db
from src.models import User  # Assuming User is a model defined in models/__init__.py

fake = Faker()

def seed_users(db: Session, num_users: int = 10):
    for _ in range(num_users):
        user = User(
            username=fake.user_name(),
            email=fake.email(),
            full_name=fake.name(),
            hashed_password=fake.password()
        )
        db.add(user)
    db.commit()

def main():
    db = get_db()
    seed_users(db)

if __name__ == "__main__":
    main()