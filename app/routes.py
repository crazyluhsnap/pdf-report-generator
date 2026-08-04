from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from fastapi.responses import FileResponse

from . import models,schemas
from .database import SessionLocal
from .report_generator import generate_pdf_report

router=APIRouter()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_summary_data(db: Session):
    total_students=db.query(
        func.count(models.Student.id)
    ).scalar()

    average_math=db.query(
        func.avg(models.Student.math)
    ).scalar()

    average_science=db.query(
        func.avg(models.Student.science)
    ).scalar()

    average_english=db.query(
        func.avg(models.Student.english)
    ).scalar()

    average_attendance=db.query(
        func.avg(models.Student.attendance)
    ).scalar()


    highest_math=db.query(
        func.max(models.Student.math)
    ).scalar()
    
    highest_science=db.query(
        func.max(models.Student.science)
    ).scalar()
    
    highest_english=db.query(
        func.max(models.Student.english)
    ).scalar()
    
    highest_attendance=db.query(
        func.max(models.Student.attendance)
    ).scalar()


    lowest_math=db.query(
        func.min(models.Student.math)
    ).scalar()
    
    lowest_science=db.query(
        func.min(models.Student.science)
    ).scalar()
    
    lowest_english=db.query(
        func.min(models.Student.english)
    ).scalar()
    
    lowest_attendance=db.query(
        func.min(models.Student.attendance)
    ).scalar()


    total_math_marks=db.query(
        func.sum(models.Student.math)
    ).scalar()
    
    total_science_marks=db.query(
        func.sum(models.Student.science)
    ).scalar()
    
    total_english_marks=db.query(
        func.sum(models.Student.english)
    ).scalar()


    return {
        "total_students": total_students,

        "average_math": average_math,
        "highest_math": highest_math,
        "lowest_math": lowest_math,
        "total_math_marks": total_math_marks,

        "average_science": average_science,
        "highest_science": highest_science,
        "lowest_science": lowest_science,
        "total_science_marks": total_science_marks,

        "average_english": average_english,
        "highest_english": highest_english,
        "lowest_english": lowest_english,
        "total_english_marks": total_english_marks,

        "average_attendance": average_attendance,
        "highest_attendance": highest_attendance,
        "lowest_attendance": lowest_attendance
    }




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


@router.get(
    "/reports/summary",
    summary="Get report summary"
)
def get_report_summary(
    db: Session=Depends(get_db)
):
    return get_summary_data(db)


@router.get(
    "/reports/pdf"
)
def generate_report(db: Session = Depends(get_db)):
    summary_data=get_summary_data(db)
    filepath=generate_pdf_report(summary_data)

    return FileResponse(
        path=filepath,
        filename="student_report.pdf",
        media_type="application/pdf"
    )