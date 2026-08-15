# Run development server
uvicorn app.main:app --reload
alembic revision --autogenerate -m ""
alembic upgrade head
python -m app.seeds.seed_data