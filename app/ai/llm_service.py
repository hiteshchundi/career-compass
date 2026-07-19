import json
import os
from dataclasses import asdict, is_dataclass

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


class LLMService:
    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("GROQ_API_KEY"),
            base_url="https://api.groq.com/openai/v1",
        )

        # You can change this later if you want
        self.model = "llama-3.3-70b-versatile"

    def analyze(
        self,
        resume_text: str,
        job_description: str,
        baseline_result,
    ):

        if is_dataclass(baseline_result):
            baseline_result = asdict(baseline_result)

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
You are an experienced technical recruiter.

Evaluate the resume against the job description.

Use semantic understanding.

Do NOT rely only on keywords.

Resume

{resume_text}

---------------------------------------

Job Description

{job_description}

---------------------------------------

Rule Based Analysis

{baseline_json}

---------------------------------------

Return ONLY valid JSON.

{{
    "match_score": 85,
    "matched_skills": [],
    "missing_skills": [],
    "experience_match": true,
    "education_match": true,
    "recommendations": [],
    "summary": ""
}}
"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            temperature=0.3,
        )

        content = response.choices[0].message.content.strip()

        if content.startswith("```"):
            lines = content.splitlines()

            if lines[0].startswith("```"):
                lines = lines[1:]

            if lines[-1].startswith("```"):
                lines = lines[:-1]

            content = "\n".join(lines)

        return json.loads(content)

    def tailor_resume(
        self,
        resume_text: str,
        job_description: str,
    ):

        prompt = f"""
You are a senior recruiter.

Rewrite this resume so it better matches the job description.

Rules:

- Never invent companies.
- Never invent experience.
- Never invent education.
- Never invent projects.
- Never invent skills.
- Improve wording.
- Use stronger action verbs.
- Optimize for ATS.

Resume

{resume_text}

---------------------------------------

Job Description

{job_description}

---------------------------------------

Return ONLY the rewritten resume.
"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            temperature=0.4,
        )

        return response.choices[0].message.content