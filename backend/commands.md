



# Run development server
uvicorn app.main:app --reload
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
# Alembic commands
alembic revision --autogenerate -m ""
alembic upgrade head
alembic current

# Docker commands
$ docker compose --env-file .env.docker up -d
# Seed the data
python -m app.seeds.seed_data