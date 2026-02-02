from sqlalchemy.orm import Session
from faker import Faker
from src.SQLAlchemy.connection import SessionLocal

fake = Faker()

def seed_users(db: Session, num_users: int = 10):
    """Seed the database with fake user data"""
    try:
        from src.models import User
        for _ in range(num_users):
            user = User(
                username=fake.user_name(),
                email=fake.email(),
                full_name=fake.name(),
                hashed_password=fake.password()
            )
            db.add(user)
        db.commit()
        print(f"Successfully seeded {num_users} users")
    except Exception as e:
        db.rollback()
        print(f"Error seeding users: {e}")

def main():
    """Main function to run seeds"""
    db = SessionLocal()
    seed_users(db)
    db.close()

if __name__ == "__main__":
    main()
