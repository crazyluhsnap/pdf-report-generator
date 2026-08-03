from fastapi import APIRouter, Depends, HTTPException
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


@router.get(
    "/students",
    response_model=list[schemas.StudentResponse],
    summary="Get all students"
)
def get_students(
    db:Session=Depends(get_db)
):
    students=db.query(models.Student).all()

    return students


@router.get(
    "/students/{student_id}",
    response_model=schemas.StudentResponse,
    summary="Get student by ID"
)
def get_student(
    student_id:int,
    db:Session=Depends(get_db)
):
    student=db.query(models.Student).filter(
        models.Student.id==student_id
    ).first()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student

