from fastapi import FastAPI
from app.api import auth, employees, students, school_classes, student_history

app = FastAPI()

app.include_router(auth.router)
app.include_router(employees.router)
app.include_router(students.router)
app.include_router(school_classes.router)
app.include_router(student_history.router)





if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)