from fastapi import FastAPI
from app.api import auth, employees, students, school_classes, student_history, room, subject, subject_assignment
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://super-journey-g4x49w79xvxgh99rp-5173.app.github.dev",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(employees.router)
app.include_router(students.router)
app.include_router(school_classes.router)
app.include_router(student_history.router)
app.include_router(room.router)
app.include_router(subject.router)
app.include_router(subject_assignment.router)





if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)