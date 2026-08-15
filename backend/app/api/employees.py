
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.auth import UserUpdate
from app.services.services import update_user_info, archive_user, get_teacher_info, get_stuff_info, get_employees_info
from app.db.dependencies import get_db
from app.repositories.user_repository import get_user_by_id
from app.models.user import User
from app.models.employee import Employee_Type
from app.auth.jwt import get_current_user

router = APIRouter(prefix="/employees", tags=["Employees"])

@router.put("/{user_id}")
def update(user_data: UserUpdate,
           user_id:int,
            db:Session = Depends(get_db), 
            current_user: User = Depends(get_current_user)):
    if current_user.role.name =="SuperAdmin":
        try:
            return update_user_info(db=db, user_data=user_data, user=get_user_by_id(db, user_id))
            
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

    else: 
        raise HTTPException(status_code=403, detail="You do not have permission to update a user.")


@router.patch("/{user_id}/archive")
def archive(user_id:int, db:Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if current_user.role.name =="SuperAdmin":
            try:
                return archive_user(db, user= get_user_by_id(db, user_id))
            
            except ValueError as e:
                raise HTTPException(status_code=400, detail=str(e))
    
    else: 
            raise HTTPException(status_code=404, detail="You do not have permission to archive a user.")
    
    
@router.get("/me")
def get_user(db:Session = Depends(get_db), current_user: User=Depends(get_current_user)):
     if current_user:
          try:
               if current_user.employee is not None and current_user.employee.employee_type == Employee_Type.TEACHER:
                return get_teacher_info(db, current_user)
               
               return get_stuff_info(db, current_user)
          except ValueError as e:
               raise HTTPException(status_code=400, detail=str(e))

     else:
          
        raise HTTPException(status_code=404, detail="Seems Like user is deactivated or not valid.")
        

@router.get("/")
def get_employees(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if not current_user or not current_user.is_active:
        raise HTTPException(
            status_code=403,
            detail="User is deactivated or not valid."
        )
    if current_user.role.name not in ["SuperAdmin", "Admin"]:
        return None
    return get_employees_info(db)
    

