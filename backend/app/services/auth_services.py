from app.schemas.auth import UserCreate
from app.models.employee import Employee
from app.models.teacher import Teacher
from app.auth.hashing import hash_password, verify_password
from datetime import datetime, timedelta, timezone
from app.settings.settings import settings
import jwt
from app.models.user import User
from app.repositories.user_repository import create, email_exists, username_exists, get_user_by_email, get_user_by_username
from app.repositories.role_repository import get_role_by_name
from sqlalchemy.orm import Session

def register_user(db: Session, user_data: UserCreate):
    email_already_exists = email_exists(db, user_data.email)
    username_already_exists = username_exists(db, user_data.username)
    role = get_role_by_name(db, "User")
    if role is None:
        raise ValueError("User role does not exist. Run seed_roles.py first.")

    if email_already_exists:
        raise ValueError("Email already exists.")

    if username_already_exists:
        raise ValueError("Username already exists.")

    if len(user_data.password) < 8:
        raise ValueError("Password must be at least 8 characters long.")

    hashed_password = hash_password(user_data.password)

    # Create User
    user = User(
        role_id=role.id,
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        email=user_data.email,
        username=user_data.username,
        password_hash=hashed_password
    )
    employee = Employee(
        user = user,
        employee_type=user_data.employee_type,
        hire_date=user_data.hire_date,

    )
    if user_data.employee_type == "TEACHER":
        teacher = Teacher(
            employee=employee
        )
    # Save User
    return create(db, user)

def login_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user:
        raise ValueError("Invalid email or password.")
    if not verify_password(password, user.password_hash):
        raise ValueError("Invalid email or password.")
    return user


def create_access_token(data: dict, expires_minutes: int):


    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=expires_minutes)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt