
from sqlalchemy.orm import Session

from app.db.db import SessionLocal
from app.models.role import Role

from app.repositories.role_repository import role_exists, create as create_role_repo
from app.models.role import Role

roles = [
    "SuperAdmin",
    "Admin",
    "User",
    ]
def seed_roles():
    db: Session = SessionLocal()

    try: 
        for role_name in roles:
            if not role_exists(db, role_name):
                create_role_repo(db, Role(name=role_name))


    finally:
        db.close()
if __name__ == "__main__":
    seed_roles()
    