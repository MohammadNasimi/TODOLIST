from fastapi import Depends, FastAPI

from typing import Annotated

from dependencies import get_query_token, get_token_header
from internal import admin
from routers import tasks, users
from database import get_session

# import models 
from models.users import Users
from models.tasks import Tasks
# db
from database import create_db_and_tables, get_session, Session


app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


app.include_router(users.router)
app.include_router(tasks.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}