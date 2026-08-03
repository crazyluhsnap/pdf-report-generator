from sqlalchemy import Column, Integer, String, Float

from .database import Base

class Student(Base):
    __tablename__="students"

    id=Column(Integer, primary_key=True, index=True)

    name=Column(String, nullable=False)
    department=Column(String, nullable=False)
    semester=Column(Integer, nullable=False)

    math=Column(Integer, nullable=False)
    science=Column(Integer, nullable=False)
    english=Column(Integer, nullable=False)

    attendance=Column(Float, nullable=False)