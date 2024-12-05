from sqlmodel import Field, SQLModel,Relationship
from passlib.hash import bcrypt


class Users(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    email: str | None = Field(default=None, index=True, unique=True)
    password: str
    tasks: list["Tasks"] = Relationship(back_populates="user")  # Relationship to Tasks

    def set_password(self, password: str):
        self.password = bcrypt.hash(password)


    def verify_password(self, password: str) -> bool:
        return bcrypt.verify(password, self.password)