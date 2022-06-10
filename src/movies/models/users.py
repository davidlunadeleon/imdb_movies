from movies.models import Base
from sqlalchemy import (
    Column,
    Integer,
    String,
    TIMESTAMP,
)


class User(Base):
    __tablename__ = "users"

    create_time = Column(TIMESTAMP(timezone=True), index=True)
    password_hash = Column(String)
    preference_key = Column(Integer)
    user_id = Column(Integer, primary_key=True)
    username = Column(String)
