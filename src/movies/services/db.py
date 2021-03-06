from sqlalchemy import (
    Column,
    Float,
    Integer,
    LargeBinary,
    MetaData,
    String,
    TIMESTAMP,
    Table,
    UniqueConstraint,
    create_engine,
)
from sqlalchemy.orm import mapper, sessionmaker, Session
import os

from movies.models.movies import Movie
from movies.models.users import User


def get_postgres_uri():
    # Progress setup
    host = os.environ.get("DB_HOST", "postgres")
    port = 5432
    password = os.environ.get("DB_PASS", "abc123")
    user, db_name = "movies", "movies"
    return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"


engine = create_engine(
    get_postgres_uri(),
    isolation_level="REPEATABLE READ",
)

metadata = MetaData()

# Movies' table
movies = Table(
    "movies",
    metadata,
    Column("movie_id", Integer, primary_key=True, autoincrement=True),
    Column("create_time", TIMESTAMP(timezone=True), index=True),
    Column("movie_title", String),
    Column("preference_key", Integer),
    Column("rating", Float),
    Column("year", Integer),
)

# Users' table
users = Table(
    "users",
    metadata,
    Column("user_id", Integer, primary_key=True, autoincrement=True),
    Column("create_time", TIMESTAMP(timezone=True), index=True),
    Column("password_hash", LargeBinary),
    Column("preference_key", Integer),
    Column("username", String),
    UniqueConstraint("username"),
)


def start_mappers() -> Session:
    movies_mapper = mapper(Movie, movies)
    users_mapper = mapper(User, users)
    metadata.create_all(engine)
    return sessionmaker(bind=engine)()
