# Career Compass

An AI-powered resume analysis platform built with **FastAPI**, **PostgreSQL**, and **React** (frontend coming soon).

Career Compass helps users understand their resumes by extracting structured information such as skills, experience, education, projects, and certifications. Future versions will compare resumes against job descriptions, identify skill gaps, provide ATS optimization suggestions, and generate AI-powered recommendations.

---

## Project Status

**Current Version:** v0.1.0

### ✅ Completed

* FastAPI backend
* PostgreSQL integration
* SQLAlchemy ORM
* Alembic database migrations
* Layered architecture (Router → Service → Repository)
* User management API
* Resume upload API
* PDF resume extraction
* DOCX resume extraction
* Resume text normalization
* File storage system
* End-to-end resume ingestion pipeline

### 🚧 In Progress

* Resume Analysis Engine

### 📌 Planned

* Structured resume parsing
* Job description analysis
* Resume-job matching
* ATS score generation
* AI-powered resume recommendations
* Clean React frontend

---

# Architecture

```
Client
    │
    ▼
FastAPI
    │
    ▼
Routers
    │
    ▼
Services
    │
    ▼
Repositories
    │
    ▼
SQLAlchemy ORM
    │
    ▼
PostgreSQL
```

---

# Tech Stack

### Backend

* Python 3.14
* FastAPI
* SQLAlchemy 2.0
* PostgreSQL
* Alembic
* Pydantic

### Resume Processing

* pypdf
* python-docx

### Frontend (Planned)

* React
* TypeScript
* Vite
* Tailwind CSS
* shadcn/ui

---

# Current Features

## User Management

* Create users
* Retrieve users
* Email uniqueness validation

## Resume Upload

* Upload PDF resumes
* Upload DOCX resumes
* Automatic text extraction
* Text normalization
* Store uploaded files
* Persist extracted resume data

---

# Project Structure

```
app/
├── api/
├── db/
├── ingestion/
├── repositories/
├── schemas/
├── services/
├── storage/
└── utils/
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

## Activate

macOS/Linux

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Configure environment

Create a `.env` file.

Example:

```
DATABASE_URL=postgresql+psycopg://username:password@localhost/career_compass
```

## Run migrations

```bash
alembic upgrade head
```

## Start the application

```bash
uvicorn app.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

# Roadmap

## Phase 1

* ✅ Resume upload
* 🚧 Resume analysis

## Phase 2

* Job description parsing
* Structured job representation

## Phase 3

* Resume-job matching
* Skill gap analysis
* ATS scoring

## Phase 4

* AI recommendations
* Resume tailoring
* Cover letter generation

---

# License

MIT License
