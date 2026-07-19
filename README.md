# Career Compass

Career Compass is an AI-assisted career platform that helps job seekers understand their resumes through structured analysis. It extracts key information such as contact details, skills, education, and experience, providing the foundation for resume optimization and job matching.

Built for rapid iteration using **FastAPI**, **PostgreSQL**, and **React**.

---

# Demo Features

### ✅ Resume Upload

* Upload PDF resumes
* Upload DOCX resumes
* Secure file storage

### ✅ Resume Processing

* Extract text from PDF resumes
* Extract text from DOCX resumes
* Normalize extracted text

### ✅ Resume Analysis

* Extract contact information
* Extract technical skills
* Structured resume analysis schema
* Deterministic parsing engine

### ✅ Backend

* REST API with FastAPI
* PostgreSQL database
* SQLAlchemy ORM
* Alembic migrations
* Layered architecture
* Unit tests

---

# Tech Stack

## Backend

* Python 3.14
* FastAPI
* PostgreSQL
* SQLAlchemy 2.0
* Alembic
* Pydantic

## Resume Processing

* pypdf
* python-docx
* Regular Expressions

## Frontend

* React
* TypeScript
* Vite
* Tailwind CSS

---

# Architecture

```
                Resume Upload
                      │
                      ▼
            PDF / DOCX Extraction
                      │
                      ▼
          Resume Analysis Engine
                      │
                      ▼
          Structured Resume Data
                      │
                      ▼
                FastAPI API
                      │
                      ▼
                PostgreSQL
                      │
                      ▼
                 React Frontend
```

---

# Current Project Structure

```
app/
├── api/
├── db/
├── ingestion/
├── repositories/
├── resume_analysis/
├── schemas/
├── services/
├── storage/
└── utils/

tests/
```

---

# Getting Started

## Clone the repository

```bash
git clone <repository-url>
cd career-compass
```

## Create a virtual environment

```bash
python -m venv .venv
```

## Activate the environment

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Configure environment

Create a `.env` file.

```env
DATABASE_URL=postgresql+psycopg://username:password@localhost/career_compass
```

## Run database migrations

```bash
alembic upgrade head
```

## Start the server

```bash
uvicorn app.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

# Development Progress

## ✅ Completed

* FastAPI backend
* PostgreSQL integration
* SQLAlchemy ORM
* Alembic migrations
* User management API
* Resume upload API
* PDF extraction
* DOCX extraction
* Text normalization
* Resume analysis schema
* Resume parser
* Contact extraction
* Skills extraction
* Unit testing

## 🚧 In Progress

* Education extraction
* Experience extraction
* Resume analysis endpoint
* React dashboard

## 🔜 Next

* Resume vs Job Description matching
* Skill gap analysis
* ATS score
* AI-powered resume recommendations
* Resume tailoring
* Cover letter generation

---

# Hackathon Vision

Career Compass aims to become an intelligent career assistant that helps job seekers:

* Understand their resumes
* Identify missing skills
* Match resumes against job descriptions
* Improve ATS compatibility
* Receive AI-powered career recommendations

---

# License

MIT License
