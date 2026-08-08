
from sqlalchemy.orm import Session

from app.db.db import SessionLocal
from app.auth.hashing import hash_password
from app.repositories.user_repository import username_exists, email_exists, create as create_user_repo
from app.repositories.role_repository import get_role_by_name
from app.models.user import User
from app.settings.settings import settings




def seed_superadmin():
        db: Session = SessionLocal()
        

        try:
            role = get_role_by_name(db, "SuperAdmin")
            if role is None:
                 raise ValueError("SuperAdmin role does not exist. Run seed_roles.py first.")

            # Check if superadmin already exists
            if not username_exists(db, settings.SUPERADMIN_USERNAME) and \
                not email_exists(db, settings.SUPERADMIN_EMAIL):
                hashed_password = hash_password(settings.SUPERADMIN_PASSWORD)
                
                    # Create User
                create_user_repo(db, 
                    User(
                    role_id= role.id,
                    first_name=settings.SUPERADMIN_FIRST_NAME,
                    last_name=settings.SUPERADMIN_LAST_NAME,
                    email=settings.SUPERADMIN_EMAIL,
                    username=settings.SUPERADMIN_USERNAME,
                    password_hash=hashed_password
                    ))
        finally:
            db.close()
              
if __name__ == "__main__":
    seed_superadmin()
    