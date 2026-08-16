



# Run development server
uvicorn app.main:app --reload
# Alembic commands
alembic revision --autogenerate -m ""
alembic upgrade head

# Seed the data
python -m app.seeds.seed_data