
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.student import StudentUpdate, StudentResponse, StudentCreate
from app.services.student_services import create_student, update_student_info, get_student_by_id, get_student_info, delete_student_id, get_students_info
from app.db.dependencies import get_db
from app.repositories.student_repository import get_student_by_email, get_student_by_id
from app.models.student import Student
from app.models.user import User
from app.auth.jwt import get_current_user

router = APIRouter(prefix="/students", tags=["Students"])



@router.post("/create", response_model=StudentResponse)
def create(student_data: StudentCreate, db:Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if current_user.role.name not in ["SuperAdmin", "Admin"]:
        raise HTTPException(status_code=403, detail="You do not have permission to create a new student.")

    try:
        student = create_student(db, student_data)
        return student
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{email}")
def update(student_data: StudentUpdate,
           student_id:int,
            db:Session = Depends(get_db), 
            current_user: User = Depends(get_current_user)):
    if not current_user.role.name in ["SuperAdmin", "Admin"]:
        
        raise HTTPException(status_code=403, detail="You do not have permission to update a student.") 

    try:
        return update_student_info(db=db, student_data=student_data, student=get_student_by_id(db, student_id))
                
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{student_id}")
def delete(student_id:int, db:Session=Depends(get_db), current_user: User = Depends(get_current_user)):
    if current_user.role.name not in ["SuperAdmin", "Admin"]:
        raise HTTPException(status_code=403, detail="You do not have permission to delete a student.")

    return delete_student_id(db, student_id)

@router.get("/")
def get_students(db:Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    return get_students_info(db)

@router.get("/{email}", response_model=StudentResponse)
def get_student(
    email: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)

):
    return get_student_info(db, email)