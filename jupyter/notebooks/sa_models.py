import sqlalchemy as sa
import sqlalchemy.orm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String)
    messages = sa.orm.relationship("Message", back_populates="user")


class Message(Base):
    __tablename__ = "messages"

    id = sa.Column(sa.Integer, primary_key=True)
    content = sa.Column(sa.String)
    user = sa.orm.relationship("User", back_populates="messages")
    user_id = sa.Column(sa.Integer, sa.ForeignKey("users.id"))

    @classmethod
    def from_user_sync(cls, session: sa.orm.Session, user_name: str):
        statement = sa.select(cls).join(User).where(User.name == user_name)
        results = session.execute(statement)
        return results.scalars().all()

    @classmethod
    async def from_user_async(cls, session: AsyncSession, user_name: str):
        statement = sa.select(cls).join(User).where(User.name == user_name)
        results = await session.execute(statement)
        return results.scalars().all()
