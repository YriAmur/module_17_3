from fastapi import FastAPI
from app.routers import task, user
import app.models.user as user_model
import app.models.task as task_model

app = FastAPI()

@app.get('/')
async def welcome():
    return {"message": "Welcome to Taskmanager"}

app.include_router(task.router)
app.include_router(user.router)




# pip install fastapi[all]
# pip install sqlalchemy
# pip install alembic
# alembic init app/migrations
# alembic revision - -autogenerate - m "Initial migration"
# alembic upgrade head

# uvicorn app.main:app