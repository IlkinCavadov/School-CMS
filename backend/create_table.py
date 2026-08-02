from app.db.db import engine
from app.models.base import Base

# Import all models so SQLAlchemy knows about them
from app.models.role import Role

Base.metadata.create_all(bind=engine)

print("Tables created successfully.")