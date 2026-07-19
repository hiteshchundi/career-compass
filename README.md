# 🧭 Career Compass

> AI-powered resume analysis, ATS scoring, skill gap detection, and resume tailoring.

Career Compass helps job seekers understand how well their resume matches a job description before they apply.

Instead of blindly submitting resumes, users receive:

- 📊 Resume-to-job match score
- 🎯 ATS compatibility score
- ✅ Matching skills
- ❌ Missing skills
- 💡 Personalized improvement suggestions
- 📄 AI-tailored resume for the selected job

Built for the hackathon using **FastAPI**, **React**, **TypeScript**, and **Google Gemini**.

---

# 🚀 Live Demo

### Frontend

**https://career-compass-hitzhraj.vercel.app**

### Backend API

**https://career-compass-jn9h.onrender.com/docs**

---

# ✨ Features

## Resume Analysis

Upload a resume and paste a job description.

Career Compass analyzes:

- Resume relevance
- ATS compatibility
- Skill overlap
- Missing keywords
- Overall job match

---

## ATS Match Score

Receive an overall percentage indicating how well the resume aligns with the job description.

Example:

```
Resume Match: 86%

ATS Score: 91%
```

---

## Skill Gap Detection

Automatically identifies

- Skills found in the resume
- Skills required by the job
- Missing skills

Example

```
Present Skills

✔ Python
✔ SQL
✔ Pandas
✔ Tableau

Missing Skills

✖ Airflow
✖ Docker
✖ AWS
```

---

## Resume Improvement Suggestions

Career Compass generates personalized recommendations such as

- Missing keywords
- Better resume wording
- Skills to highlight
- ATS optimization tips

---

## AI Resume Tailoring

Generate a tailored version of your resume specifically for the selected job description while preserving your actual experience.

The tailored resume is downloadable as a PDF.

---

# 🏗️ Tech Stack

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

- Google Gemini

## Deployment

- Vercel
- Render

---

# 📂 Project Structure

```
career-compass/
│
├── frontend/
│   ├── src/
│   └── public/
│
├── app/
│   ├── api/
│   ├── services/
│   ├── ingestion/
│   ├── ai/
│   └── schemas/
│
├── tests/
│
└── README.md
```

---

# ⚙️ Local Setup

## Clone

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

Backend runs on

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

Frontend runs on

```
http://localhost:5173
```

---

# 🔑 Environment Variables

Backend

```
GOOGLE_API_KEY=your_google_gemini_api_key
```

Frontend

```
VITE_API_URL=http://127.0.0.1:8000
```

Production

```
VITE_API_URL=https://career-compass-jn9h.onrender.com
```

---

# 📸 Demo Flow

1. Upload resume
2. Paste job description
3. Click **Analyze Resume**
4. Review

- Match Score
- ATS Score
- Matching Skills
- Missing Skills
- Suggestions

5. Click **Generate Tailored Resume**
6. Download the customized resume

---

# 🎯 Future Roadmap

- Multiple resume management
- Job URL parsing
- Cover letter generation
- Interview question generation
- Resume version history
- Authentication
- Dashboard & analytics
- Job application tracking

---

# 👨‍💻 Author

**Hitesh Chundi**

GitHub

https://github.com/hiteshchundi

---

# 🙏 Acknowledgements

- Google Gemini
- FastAPI
- React
- Vite
- Render
- Vercel

---

# ⭐ If you found this project interesting, consider giving it a star!
