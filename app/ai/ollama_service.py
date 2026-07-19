from dataclasses import asdict, is_dataclass
import json

from ollama import Client


class OllamaService:
    def __init__(self):
        self.client = Client(
            host="http://localhost:11434"
        )

    def analyze(
        self,
        resume_text: str,
        job_description: str,
        baseline_result,
    ):
        # Convert MatchResult dataclass
        if is_dataclass(baseline_result):
            baseline_result = asdict(baseline_result)

        # Future-proof for Pydantic
        elif hasattr(baseline_result, "model_dump"):
            baseline_result = baseline_result.model_dump()

        elif hasattr(baseline_result, "dict"):
            baseline_result = baseline_result.dict()

        baseline_json = json.dumps(
            baseline_result,
            indent=2,
            ensure_ascii=False,
        )

        prompt = f"""
You are an experienced technical recruiter, hiring manager, and ATS evaluator.

Your task is to determine how well this candidate matches the job description.

Think like a real recruiter.

Do NOT rely only on exact keyword matching.
Understand semantic similarity between technologies and transferable skills.

Examples:

- PostgreSQL = SQL
- MySQL = SQL
- SQL Server = SQL
- FastAPI = REST API Development
- Flask = Backend Development
- Pandas + NumPy = Data Analysis
- Docker Compose = Docker
- GitHub = Git
- Jenkins = CI/CD

Use the rule-based analysis only as a reference.
If you disagree with it, provide your own judgement.

--------------------------------------------------
RESUME
--------------------------------------------------

{resume_text}

--------------------------------------------------
JOB DESCRIPTION
--------------------------------------------------

{job_description}

--------------------------------------------------
RULE-BASED ANALYSIS
--------------------------------------------------

{baseline_json}

--------------------------------------------------

Evaluate and determine:

1. ATS Match Score (0-100)

2. Skills already demonstrated that satisfy the job.

3. Important missing skills.

4. Whether the candidate satisfies the required experience.

5. Whether the candidate satisfies the education requirement.

6. Practical recommendations for improving the resume.

7. A concise recruiter summary explaining your decision.

Return ONLY valid JSON.

{{
    "match_score": 85,
    "matched_skills": [
        "Python",
        "SQL"
    ],
    "missing_skills": [
        "Docker",
        "AWS"
    ],
    "experience_match": true,
    "education_match": true,
    "recommendations": [
        "Highlight SQL projects.",
        "Add Docker experience."
    ],
    "summary": "The candidate demonstrates strong backend development skills with Python and SQL. Experience aligns well with the role, but Docker and AWS exposure would strengthen the application."
}}
"""

        response = self.client.chat(
            model="qwen2.5:7b",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        content = response["message"]["content"].strip()

        # Remove markdown fences if present
        if content.startswith("```"):
            lines = content.splitlines()

            if lines and lines[0].startswith("```"):
                lines = lines[1:]

            if lines and lines[-1].startswith("```"):
                lines = lines[:-1]

            content = "\n".join(lines)

        return json.loads(content)

    def tailor_resume(
        self,
        resume_text: str,
        job_description: str,
    ):
        prompt = f"""
You are a senior technical recruiter.

Rewrite the resume so that it better aligns with the job description.

Rules:

- Never invent companies.
- Never invent experience.
- Never invent projects.
- Never invent education.
- Never invent skills.
- Improve wording.
- Use stronger action verbs.
- Optimize for ATS.
- Preserve the original meaning.
- Keep everything truthful.

--------------------------------------------------
RESUME
--------------------------------------------------

{resume_text}

--------------------------------------------------
JOB DESCRIPTION
--------------------------------------------------

{job_description}

--------------------------------------------------

Return ONLY the rewritten resume.

Do not include explanations.
"""

        response = self.client.chat(
            model="qwen2.5:7b",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response["message"]["content"].strip()