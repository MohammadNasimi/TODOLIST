from fastapi import APIRouter
from database import SessionDep
from schema.users import UserCreate, UserRead
from models.users import Users
router = APIRouter()


@router.post("/create/user")
def create_hero(user: UserCreate, session: SessionDep) -> Users:
    db_user = Users.from_orm(user)  # Convert Pydantic model to SQLModel
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


@router.get("/users/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}