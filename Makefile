run:
	@uvicorn workout_api.main:app --reload

create-migrations:
	@set "PYTHONPATH=%PYTHONPATH%;$(pwd)" && alembic revision --autogenerate -m "$(d)"

run-migrations:
	@set "PYTHONPATH=%PYTHONPATH%;$(pwd)" && alembic upgrade head