from datetime import date

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.settings.settings import settings
from app.auth.hashing import hash_password

from app.models.role import Role
from app.models.user import User
from app.models.employee import Employee
from app.models.teacher import Teacher
from app.models.school_class import SchoolClass
from app.models.student import Student
from app.models.student_history import StudentHistory
from app.models.subject import Subject
from app.models.subject_assignment import SubjectAssignment
from app.models.room import Room


engine = create_engine(settings.DB_URL)
SessionLocal = sessionmaker(bind=engine)


def seed():
    db = SessionLocal()

    try:
        # =========================================================
        # ROLES
        # =========================================================

        user_role = db.query(Role).filter(Role.name == "User").first()
        admin_role = db.query(Role).filter(Role.name == "Admin").first()

        if user_role is None:
            user_role = Role(name="User")
            db.add(user_role)

        if admin_role is None:
            admin_role = Role(name="Admin")
            db.add(admin_role)

        db.flush()

        # =========================================================
        # PRINCIPAL
        # =========================================================

        principal_user = (
            db.query(User)
            .filter(User.email == "anna.mueller@school.local")
            .first()
        )

        if principal_user is None:
            principal_user = User(
                role_id=admin_role.id,
                first_name="Anna",
                last_name="Muller",
                email="anna.mueller@school.local",
                username="anna.mueller",
                password_hash=hash_password("School123!"),
            )

            db.add(principal_user)
            db.flush()

            principal_employee = Employee(
                user=principal_user,
                employee_type="PRINCIPAL",
                hire_date=date(2018, 8, 1),
                employee_number=None,
            )

            db.add(principal_employee)

        # =========================================================
        # TEACHERS
        # =========================================================

        teachers_data = [
            {
                "first_name": "Thomas",
                "last_name": "Schmidt",
                "email": "thomas.schmidt@school.local",
                "username": "thomas.schmidt",
            },
            {
                "first_name": "Laura",
                "last_name": "Weber",
                "email": "laura.weber@school.local",
                "username": "laura.weber",
            },
            {
                "first_name": "Michael",
                "last_name": "Fischer",
                "email": "michael.fischer@school.local",
                "username": "michael.fischer",
            },
            {
                "first_name": "Julia",
                "last_name": "Wagner",
                "email": "julia.wagner@school.local",
                "username": "julia.wagner",
            },
            {
                "first_name": "Daniel",
                "last_name": "Becker",
                "email": "daniel.becker@school.local",
                "username": "daniel.becker",
            },
            {
                "first_name": "Sarah",
                "last_name": "Hoffmann",
                "email": "sarah.hoffmann@school.local",
                "username": "sarah.hoffmann",
            },
            {
                "first_name": "Peter",
                "last_name": "Koch",
                "email": "peter.koch@school.local",
                "username": "peter.koch",
            },
            {
                "first_name": "Lisa",
                "last_name": "Richter",
                "email": "lisa.richter@school.local",
                "username": "lisa.richter",
            },
            {
                "first_name": "Markus",
                "last_name": "Klein",
                "email": "markus.klein@school.local",
                "username": "markus.klein",
            },
            {
                "first_name": "Sophie",
                "last_name": "Wolf",
                "email": "sophie.wolf@school.local",
                "username": "sophie.wolf",
            },
        ]

        teachers = []

        for teacher_data in teachers_data:
            user = (
                db.query(User)
                .filter(User.email == teacher_data["email"])
                .first()
            )

            if user is None:
                user = User(
                    role_id=user_role.id,
                    first_name=teacher_data["first_name"],
                    last_name=teacher_data["last_name"],
                    email=teacher_data["email"],
                    username=teacher_data["username"],
                    password_hash=hash_password("School123!"),
                )

                db.add(user)
                db.flush()

                employee = Employee(
                    user=user,
                    employee_type="TEACHER",
                    hire_date=date(2020, 8, 1),
                    employee_number=None,
                )

                db.add(employee)
                db.flush()

                teacher = Teacher(
                    user_id=user.id
                )

                db.add(teacher)
                db.flush()

            else:
                teacher = (
                    db.query(Teacher)
                    .filter(Teacher.user_id == user.id)
                    .first()
                )

                if teacher is None:
                    teacher = Teacher(
                        user_id=user.id
                    )

                    db.add(teacher)
                    db.flush()

            teachers.append(teacher)

        # =========================================================
        # SCHOOL CLASSES
        # =========================================================

        classes_data = [
            ("8A", 2025, 2026),
            ("8B", 2025, 2026),
            ("9A", 2025, 2026),
            ("9B", 2025, 2026),
            ("10A", 2025, 2026),
            ("10B", 2025, 2026),
        ]

        school_classes = []

        for index, (name, start_year, end_year) in enumerate(
            classes_data
        ):
            school_class = (
                db.query(SchoolClass)
                .filter(
                    SchoolClass.name == name,
                    SchoolClass.start_year == start_year,
                    SchoolClass.end_year == end_year,
                )
                .first()
            )

            if school_class is None:
                school_class = SchoolClass(
                    name=name,
                    start_year=start_year,
                    end_year=end_year,
                    home_teacher_id=teachers[
                        index % len(teachers)
                    ].user_id,
                )

                db.add(school_class)
                db.flush()

            school_classes.append(school_class)

        # =========================================================
        # SUBJECTS
        # =========================================================

        subjects_data = [
            (
                "Mathematics",
                "Mathematics and algebra",
            ),
            (
                "English",
                "English language and literature",
            ),
            (
                "German",
                "German language and literature",
            ),
            (
                "Physics",
                "Physics and mechanics",
            ),
            (
                "Biology",
                "Biology and life sciences",
            ),
            (
                "Chemistry",
                "Chemistry and laboratory work",
            ),
            (
                "History",
                "European and world history",
            ),
            (
                "Geography",
                "Geography and environment",
            ),
            (
                "Computer Science",
                "Programming and computer science",
            ),
            (
                "Physical Education",
                "Sports and physical education",
            ),
        ]

        subjects = []

        for name, description in subjects_data:
            subject = (
                db.query(Subject)
                .filter(Subject.name == name)
                .first()
            )

            if subject is None:
                subject = Subject(
                    name=name,
                    description=description,
                )

                db.add(subject)
                db.flush()

            subjects.append(subject)

        # =========================================================
        # ROOMS
        # =========================================================

        rooms_data = [
            (
                "101",
                25,
                "Standard classroom",
            ),
            (
                "102",
                25,
                "Standard classroom",
            ),
            (
                "103",
                30,
                "Standard classroom",
            ),
            (
                "104",
                30,
                "Standard classroom",
            ),
            (
                "105",
                30,
                "Standard classroom",
            ),
            (
                "Computer Lab",
                24,
                "Computers for programming and IT lessons",
            ),
            (
                "Physics Lab",
                20,
                "Physics laboratory",
            ),
            (
                "Chemistry Lab",
                20,
                "Chemistry laboratory",
            ),
            (
                "Biology Lab",
                20,
                "Biology laboratory",
            ),
            (
                "Gym",
                40,
                "School sports hall",
            ),
        ]

        for number, capacity, description in rooms_data:
            room = (
                db.query(Room)
                .filter(Room.number == number)
                .first()
            )

            if room is None:
                room = Room(
                    number=number,
                    capacity=capacity,
                    description=description,
                )

                db.add(room)

        db.flush()

        # =========================================================
        # STUDENTS
        # =========================================================

        students_data = [
            ("Max", "Weber", "max.weber@student.school.local"),
            ("Emma", "Schneider", "emma.schneider@student.school.local"),
            ("Leon", "Fischer", "leon.fischer@student.school.local"),
            ("Mia", "Schulz", "mia.schulz@student.school.local"),
            ("Paul", "Keller", "paul.keller@student.school.local"),
            ("Hannah", "Maier", "hannah.maier@student.school.local"),
            ("Ben", "Huber", "ben.huber@student.school.local"),
            ("Lena", "Kaiser", "lena.kaiser@student.school.local"),
            ("Finn", "Wolf", "finn.wolf@student.school.local"),
            ("Clara", "Peters", "clara.peters@student.school.local"),
            ("Jonas", "Lang", "jonas.lang@student.school.local"),
            ("Sophie", "Kraus", "sophie.kraus@student.school.local"),
            ("Noah", "Lehmann", "noah.lehmann@student.school.local"),
            ("Marie", "Bauer", "marie.bauer@student.school.local"),
            ("Elias", "Frank", "elias.frank@student.school.local"),
            ("Laura", "Zimmermann", "laura.zimmermann@student.school.local"),
            ("Felix", "Hartmann", "felix.hartmann@student.school.local"),
            ("Anna", "Schmitt", "anna.schmitt@student.school.local"),
            ("Tim", "Kuhn", "tim.kuhn@student.school.local"),
            ("Julia", "Vogel", "julia.vogel@student.school.local"),
            ("Lukas", "Kramer", "lukas.kramer@student.school.local"),
            ("Nina", "Schubert", "nina.schubert@student.school.local"),
            ("David", "Busch", "david.busch@student.school.local"),
            ("Sarah", "Lorenz", "sarah.lorenz@student.school.local"),
            ("Moritz", "Seidel", "moritz.seidel@student.school.local"),
            ("Lisa", "Jaeger", "lisa.jaeger@student.school.local"),
            ("Jan", "Brandt", "jan.brandt@student.school.local"),
            ("Amelie", "Haas", "amelie.haas@student.school.local"),
            ("Simon", "Graf", "simon.graf@student.school.local"),
            ("Marie", "Roth", "marie.roth@student.school.local"),
        ]

        for index, (first_name, last_name, email) in enumerate(
            students_data
        ):
            student = (
                db.query(Student)
                .filter(Student.email == email)
                .first()
            )

            if student is None:
                student = Student(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    start_date=date(2022, 9, 1),
                    end_date=None,
                )

                db.add(student)
                db.flush()

            school_class = school_classes[
                index % len(school_classes)
            ]

            history = (
                db.query(StudentHistory)
                .filter(
                    StudentHistory.student_id == student.id,
                    StudentHistory.student_class_id == school_class.id,
                    StudentHistory.school_year == "2025/26",
                )
                .first()
            )

            if history is None:
                history = StudentHistory(
                    student_id=student.id,
                    student_class_id=school_class.id,
                    school_year="2025/26",
                )

                db.add(history)

        # =========================================================
        # SUBJECT + TEACHER + CLASS ASSIGNMENTS
        # =========================================================

        assignments = [
            (0, 0, 0),  # Thomas   - Mathematics       - 8A
            (1, 1, 0),  # Laura    - English           - 8A
            (2, 2, 1),  # Michael  - German            - 8B
            (3, 3, 1),  # Julia    - Physics           - 8B
            (4, 4, 2),  # Daniel   - Biology           - 9A
            (5, 5, 2),  # Sarah    - Chemistry         - 9A
            (6, 6, 3),  # Peter    - History           - 9B
            (7, 7, 3),  # Lisa     - Geography         - 9B
            (8, 8, 4),  # Markus   - Computer Science  - 10A
            (9, 9, 5),  # Sophie   - Physical Education- 10B
        ]

        for teacher_index, subject_index, class_index in assignments:
            assignment = (
                db.query(SubjectAssignment)
                .filter(
                    SubjectAssignment.subject_id
                    == subjects[subject_index].id,

                    SubjectAssignment.teacher_id
                    == teachers[teacher_index].user_id,

                    SubjectAssignment.school_class_id
                    == school_classes[class_index].id,
                )
                .first()
            )

            if assignment is None:
                assignment = SubjectAssignment(
                    subject_id=subjects[subject_index].id,
                    teacher_id=teachers[teacher_index].user_id,
                    school_class_id=school_classes[class_index].id,
                )

                db.add(assignment)

        # =========================================================
        # COMMIT
        # =========================================================

        db.commit()

        print("===================================")
        print("Seed completed successfully!")
        print("1 principal")
        print("10 teachers")
        print("6 classes")
        print("10 subjects")
        print("10 rooms")
        print("30 students")
        print("10 subject assignments")
        print("===================================")

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


if __name__ == "__main__":
    seed()