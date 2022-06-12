from abc import ABC, abstractmethod
from typing import Generic, TypeVar, TypeVar, TypeVar, TypeVar
from sqlalchemy.orm import Session
from movies.models.users import User
from movies.models.movies import Movie
import csv

T = TypeVar("T", User, Movie)

# Repository Pattern

class AbstractRepository(ABC, Generic[T]):
    session: Session

    def __init__(self, session: Session):
        self.session = session

    def add(self, entity: T):
        self.session.add(entity)
        self.session.commit()

    def update(self, entity: T) -> T:
        entity = self.session.merge(entity)
        self.session.commit()
        return entity

    @abstractmethod
    def delete(self, id: int):
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, id: int) -> T:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> list[T]:
        raise NotImplementedError


class UserRepository(AbstractRepository[User]):
    def delete(self, id: int):
        self.session.query(User).filter_by(user_id=id).delete()
        self.session.commit()

    def list(self):
        return self.session.query(User).all()

    def get_by_id(self, id: int) -> User:
        return self.session.query(User).filter_by(user_id=id).one()

    def get_by_username(self, username: str) -> User:
        return self.session.query(User).filter_by(username=username).one()


class MovieRepository(AbstractRepository[Movie]):
    def delete(self, id: int):
        self.session.query(Movie).filter_by(movie_id=id).delete()
        self.session.commit()

    def list(self):
        return self.session.query(Movie).all()

    def get_by_id(self, id: int) -> Movie:
        return self.session.query(Movie).filter_by(movie_id=id).one()

    def populate(self):
        if len(self.list()) == 0:
            with open("/src/movies/movie_results.csv") as f:
                for row in csv.DictReader(f, skipinitialspace=True):
                    self.add(
                        Movie(
                            row["movie_title"],
                            int(row["preference_key"]),
                            float(row["rating"]),
                            int(row["year"]),
                        )
                    )
