from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    climate: Mapped[str] = mapped_column(String(120), nullable=True)
    population: Mapped[int] = mapped_column(nullable=True)

    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "population": self.population
        }

class People(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    gender: Mapped[str] = mapped_column(String(20), nullable=True)
    birth_year: Mapped[str] = mapped_column(String(20), nullable=True)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "birth_year": self.birth_year
        }
#Ojo CON LOS GUIONES BAJOS                      ---------------------------------------- GUIONES BAJOS------------------------------------------- GUIONES BAJOS-----------------------
class Favorite(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    planet_id: Mapped[int] = mapped_column(ForeignKey("planet.id"), nullable=True)
    people_id: Mapped[int] = mapped_column(ForeignKey("people.id"), nullable=True)

    user: Mapped["User"] = relationship(backref="favorites")
    planet: Mapped["Planet"] = relationship()
    people: Mapped["People"] = relationship()

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet": self.planet.serialize() if self.planet else None,
            "people": self.people.serialize() if self.people else None
        }