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

        # Convert MatchResult dataclass to dictionary
        if is_dataclass(baseline_result):
            baseline_result = asdict(baseline_result)

        # Convert Pydantic models if encountered
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
You are a senior technical recruiter and ATS expert.

Your task is to compare the candidate's resume with the job description.

Rules:

- Understand semantic similarity.
- Do NOT rely only on keyword matching.
- Consider transferable skills.
- Do NOT invent skills or experience.
- Improve the existing rule-based analysis.

Resume:

{resume_text}

--------------------------------------------------

Job Description:

{job_description}

--------------------------------------------------

Current Rule-Based Analysis:

{baseline_json}

--------------------------------------------------

Return ONLY valid JSON.

{{
    "match_score": 0,
    "matched_skills": [],
    "missing_skills": [],
    "recommendations": [],
    "summary": ""
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

        # Remove markdown fences if Ollama returns them
        if content.startswith("```"):
            lines = content.splitlines()

            if lines[0].startswith("```"):
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

Rewrite this resume so that it better aligns with the job description.

Rules:

- Never invent companies.
- Never invent experience.
- Never invent projects.
- Never invent education.
- Never invent skills.
- Improve wording.
- Use strong action verbs.
- Optimize for ATS.
- Keep everything truthful.

Resume:

{resume_text}

--------------------------------------------------

Job Description:

{job_description}

--------------------------------------------------

Return ONLY the rewritten resume.

Do not explain anything.
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