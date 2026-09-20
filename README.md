# Career Compass

Career Compass compares a PDF or DOCX resume with a pasted job description and can generate a tailored DOCX resume. The [frontend](https://career-compass-hitzhraj.vercel.app) is hosted on Vercel and the [API](https://career-compass-jn9h.onrender.com/docs) on Render.

## What the analysis means

The API identifies required skills, stated years of experience, and degree level in the job description. It extracts corresponding evidence from the resume and returns matching skills, missing required skills, recommendations, experience match, education match, and a match estimate. Preferred skills are parsed separately and do not lower the score.

The score is a **rule-based job match estimate**, not a score from an employer's ATS. Recognized required skills contribute 70%, experience 20%, and education 10%. Weights for requirements absent from the job description are excluded. A description with no recognizable requirements returns 0 with an explanation, rather than an artificial perfect match. Where the job explicitly accepts a degree **or** years of experience, either can satisfy that qualification. A missing requirement in the job description appears as **Not specified**, rather than **No**.

The parser recognizes a bounded skill catalog and common degree and tenure formats. It does not understand every job description or resume layout. Overlapping work periods are not added together; the longest stated tenure or date range is used. Scanned/image-only PDFs need OCR before upload. Review the extracted result and the generated resume before using either for an application.

Groq adds an optional prose summary to the deterministic analysis. If Groq is unavailable, the analysis still returns with `ai_status: "unavailable"`. Groq is required for tailored resume generation. Generation failures return HTTP 503 and a visible message. The generated file is a **DOCX**, not a PDF. AI output is not fact-verified beyond the prompt's instruction to preserve candidate facts.

## Local setup

Requires Python 3.14 and Node.js. From the repository root:

```bash
python3.14 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export GROQ_API_KEY=your_key   # needed for AI summary and tailoring
uvicorn app.main:app --reload
```

In another terminal:

```bash
cd frontend
npm install
VITE_API_URL=http://127.0.0.1:8000 npm run dev
```

Open `http://localhost:5173`. Do not commit `.env` files or API keys.

## Deployment

- Configure Render to run `uvicorn app.main:app --host 0.0.0.0 --port $PORT` with `GROQ_API_KEY` in its environment. Redeploy the backend after changes are merged to its deployed branch.
- Vercel uses `frontend` as the project root, Vite as the framework, and `VITE_API_URL=https://career-compass-jn9h.onrender.com` at build time. Redeploy after changing that variable.
- Backend CORS permits the two known Vercel domains, `career-compass-hitzhraj.vercel.app` and `career-compass-zeta-dun.vercel.app`, plus local development on port 5173. Add any future frontend domain to `app/main.py` before using it.
- `/users` and `/resumes` are not exposed because they had no authentication or ownership checks. The upload/analyze/tailor flow does not need those routes.

The Render free instance may take time to wake after inactivity. The new Groq key must be checked through a live analyze and tailor request after deployment; local tests use a synthetic resume and a mocked provider.

## API

`POST /analyze` accepts multipart fields `resume` (PDF or DOCX) and `job_description` (text). It returns JSON with `match_score`, `matched_skills`, `missing_skills`, `extra_skills`, `experience_match`, `education_match`, `education_or_experience`, `recommendations`, `summary`, and `ai_status`.

`POST /tailor` accepts the same fields and returns `tailored_resume.docx`. Unsupported files or empty job descriptions return HTTP 400. Unreadable resumes return HTTP 422. AI generation failures return HTTP 503. Temporary input and generated files are removed after processing.

## Verification

```bash
python -m pytest -q
cd frontend
npm run lint
npm run build
```

The backend suite covers skill aliases, education and experience matching, alternative qualifications, the analyze and tailor handlers, DOCX extraction, invalid input, and generated DOCX cleanup. The frontend build includes TypeScript checks. The live Groq call and production browser flow require a deployment and a synthetic upload.

## Stack

FastAPI, Pydantic, pypdf, python-docx, OpenAI-compatible Groq API, React, TypeScript, Vite, and Axios.
