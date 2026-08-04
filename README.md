# 📄 PDF Report Generator API

A RESTful API built with **FastAPI** that manages student records, performs SQL-based data aggregation, and generates professional PDF reports. The project also demonstrates asynchronous report generation using FastAPI Background Tasks.

---

## 🚀 Features

- Create student records
- Retrieve all students
- Retrieve a student by ID
- SQL aggregation using:
  - COUNT
  - AVG
  - MAX
  - MIN
  - SUM
- Generate professional PDF reports
- Download generated PDF reports
- Background PDF generation using FastAPI `BackgroundTasks`
- Interactive Swagger API documentation

---

## 🛠 Tech Stack

- **Backend:** FastAPI
- **Database:** SQLite
- **ORM:** SQLAlchemy
- **Validation:** Pydantic
- **PDF Generation:** ReportLab
- **ASGI Server:** Uvicorn

---

## 📂 Project Structure

```text
pdf-report-generator/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── routes.py
│   └── report_generator.py
│
├── generated_reports/
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/pdf-report-generator.git
cd pdf-report-generator
```

### Create virtual environment

```bash
python -m venv venv
```

### Activate virtual environment

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the server

```bash
uvicorn app.main:app --reload
```

---

## 📌 API Endpoints

<img width="1276" height="451" alt="image" src="https://github.com/user-attachments/assets/26ef2968-5120-49da-8c68-0f4450b2808e" />

---

## 📊 SQL Aggregations Used

The project demonstrates commonly used SQL aggregate functions through SQLAlchemy.

- COUNT()
- AVG()
- MAX()
- MIN()
- SUM()

---

## 📄 Sample PDF Report

<img width="792" height="576" alt="image" src="https://github.com/user-attachments/assets/c71823c3-f538-42ad-8939-de2a6737585f" />


---

## 📷 API Screenshots

<img width="1283" height="549" alt="image" src="https://github.com/user-attachments/assets/8c0e2ef0-7a6f-4b99-b0fc-437ddd8349ae" />


Example:

### Get All Students
<img width="1255" height="567" alt="image" src="https://github.com/user-attachments/assets/db3ac649-4099-49c6-a4fe-6449be242f52" />

### Add a new Student
<img width="1241" height="549" alt="image" src="https://github.com/user-attachments/assets/9299fe84-bc54-4f6e-a1d6-c7a96fbe9aa2" />

### Get a student by id
<img width="1231" height="440" alt="image" src="https://github.com/user-attachments/assets/f7467bd8-38bd-4334-8bc9-8750ae110e61" />

### Get summary of report
<img width="1253" height="545" alt="image" src="https://github.com/user-attachments/assets/baa9c6f7-8438-48e9-9c83-7d0cb9ac950d" />

### Background task
<img width="1240" height="489" alt="image" src="https://github.com/user-attachments/assets/b275ba96-10af-4361-81a7-30b71be996c3" />


### Download the PDF
<img width="1239" height="519" alt="image" src="https://github.com/user-attachments/assets/af1defa8-f838-452e-91c0-51d7ec4ca71b" />

### Downloaded PDF
<img width="792" height="576" alt="image" src="https://github.com/user-attachments/assets/81be2646-7a2c-4f2b-8952-615507c4d5a3" />



---

## 🎯 Learning Outcomes

Through this project I learned:

- REST API development with FastAPI
- SQLAlchemy ORM
- SQLite database integration
- Pydantic schema validation
- SQL aggregation functions
- Dynamic PDF generation using ReportLab
- Background task execution in FastAPI
- Clean project structure and Git workflow

---
