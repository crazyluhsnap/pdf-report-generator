from fastapi import FastAPI

app=FastAPI(
    title="PDF Report Generator API",
    description="""
A RESTful API built using FastAPI that generates PDF reports
from SQL data and processes report generation as a background task.

Feature:
- Generate PDF Reports
- Background Report Generation
- Download Generated Reports
""",
    version="1.0.0"
)

@app.get(
    "/",
    summary="Get API information"
)
def home():
    return{
        "message":"PDF Report Generator API"
    }