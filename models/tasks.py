
from sqlmodel import Field, SQLModel,Relationship
from models.users import Users

class Tasks(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    content: str
    user_id: int = Field(foreign_key="users.id")  # Correcting foreign key reference
    user: Users = Relationship(back_populates="tasks")  # Relationship to Users