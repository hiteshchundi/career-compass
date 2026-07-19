# 🧭 Career Compass

> **AI-powered Resume Analyzer & ATS Optimizer**
>
> Analyze your resume against any job description, identify missing skills, improve ATS compatibility, and generate a tailored resume—all in seconds.

---

# 🚀 Live Demo

### 🌐 Hosted Application

https://career-compass-hitzhraj.vercel.app

### 📘 Backend API Documentation

https://career-compass-jn9h.onrender.com/docs

### 💻 GitHub Repository

https://github.com/hiteshchundi/career-compass

---

# 📌 Problem Statement

Applying for jobs has become increasingly difficult due to Applicant Tracking Systems (ATS) and highly competitive job markets.

Most candidates don't know:

- Why their resume gets rejected
- Which skills they're missing
- Whether they're a good fit for a particular role
- How to tailor their resume without rewriting everything manually

Career Compass solves this by providing intelligent resume analysis powered by Large Language Models.

---

# ✨ Features

## 📊 Resume Match Analysis

Upload your resume and paste a job description to receive an overall compatibility score.

---

## 🎯 ATS Compatibility Score

Estimate how ATS-friendly your resume is based on:

- Relevant keywords
- Skill alignment
- Resume content

---

## ✅ Skills Match

Automatically identifies:

- Matching skills
- Missing skills
- Important keywords

---

## 💡 AI Suggestions

Receive personalized recommendations to improve your resume, including:

- Missing technologies
- Better wording
- ATS optimization tips
- Resume improvements

---

## 📄 AI Resume Tailoring

Generate a tailored version of your resume specifically for the selected job description while preserving your genuine experience.

The customized resume can be downloaded as a PDF.

---

# 🛠 Tech Stack

## Frontend

- React
- TypeScript
- Vite
- Axios

## Backend

- FastAPI
- Python
- PyMuPDF
- python-docx

## AI

- Groq API
- Llama 3.3 70B Versatile
- OpenAI Python SDK (Groq-compatible endpoint)

## Deployment

- Vercel (Frontend)
- Render (Backend)

---

# 🏗 Architecture

```
                +----------------------+
                |      React UI        |
                |      (Vercel)        |
                +----------+-----------+
                           |
                           |
                    REST API Calls
                           |
                           ▼
                +----------------------+
                |      FastAPI         |
                |      (Render)        |
                +----------+-----------+
                           |
        +------------------+------------------+
        |                                     |
        ▼                                     ▼
 Resume Parsing                     AI Analysis Engine
(PDF / DOCX)                      (Groq + Llama 3.3)
        |                                     |
        +------------------+------------------+
                           |
                           ▼
              Analysis + Tailored Resume
```

---

# 📸 How It Works

1. Upload your resume
2. Paste a job description
3. Click **Analyze Resume**
4. Review:
   - Resume Match Score
   - ATS Score
   - Matching Skills
   - Missing Skills
   - Improvement Suggestions
5. Generate a tailored resume
6. Download the customized PDF

---

# ⚙ Local Installation

## Clone the repository

```bash
git clone https://github.com/hiteshchundi/career-compass.git

cd career-compass
```

---

## Backend

```bash
python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Backend:

```
http://127.0.0.1:8000
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend:

```
http://localhost:5173
```

---

# 🔑 Environment Variables

Backend

```env
GROQ_API_KEY=your_groq_api_key
```

Frontend

Development

```env
VITE_API_URL=http://127.0.0.1:8000
```

Production

```env
VITE_API_URL=https://career-compass-jn9h.onrender.com
```

---

# 🚀 Future Enhancements

- Authentication & User Profiles
- Resume History
- Multiple Resume Management
- Cover Letter Generator
- Interview Question Generator
- Job URL Analysis
- Resume Version Comparison
- Application Tracker
- Career Skill Roadmaps

---

# 👨‍💻 Developer

**Hitesh Chundi**

GitHub:
https://github.com/hiteshchundi

---

# 🙏 Acknowledgements

- Groq
- Meta Llama
- FastAPI
- React
- Vite
- Render
- Vercel

---

## ⭐ Why Career Compass?

Career Compass isn't just a resume parser.

It acts as an AI career assistant that helps candidates understand **how well they fit a job, what skills they're missing, and how to improve their chances of getting shortlisted** before they ever click **Apply**.

---

**If you like this project, consider giving it a ⭐ on GitHub!**
