from typing import List, Optional

import sqlalchemy as sa
import sqlalchemy.orm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import Field, Relationship, SQLModel


class Base(SQLModel):
    id: int = Field(default=None, primary_key=True)


class User(Base, table=True):
    name: str
    messages: List["Message"] = Relationship(back_populates="user")


class Message(Base, table=True):
    content: str
    user: User = Relationship(back_populates="messages")
    user_id: int = Field(default=None, foreign_key="user.id")

    @classmethod
    def from_user(cls, session: sa.orm.Session, user_name: str):
        statement = sa.select(cls).join(User).where(User.name == user_name)
        results = session.execute(statement)
        return results.scalars().all()

    @classmethod
    async def afrom_user(cls, session: AsyncSession, user_name: str):
        statement = sa.select(cls).join(User).where(User.name == user_name)
        results = await session.execute(statement)
        return results.scalars().all()
