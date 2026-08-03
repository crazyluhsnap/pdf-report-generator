from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from . import models,schemas
from .database import SessionLocal

router=APIRouter()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post(
    "/students",
    response_model=schemas.StudentResponse,
    status_code=201,
    summary="Create a new student"
)
def create_student(
    student: schemas.StudentCreate,
    db: Session=Depends(get_db)
):
    new_student=models.Student(
        name=student.name,
        department=student.department,
        semester=student.semester,
        math=student.math,
        science=student.science,
        english=student.english,
        attendance=student.attendance
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student