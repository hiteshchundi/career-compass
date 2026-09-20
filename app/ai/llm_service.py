import json
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


class AIUnavailableError(Exception):
    """The configured AI provider could not complete the request."""


class LLMService:
    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise AIUnavailableError("GROQ_API_KEY is not configured")
        self.client = OpenAI(api_key=api_key, base_url="https://api.groq.com/openai/v1")
        self.model = "llama-3.3-70b-versatile"

    def _complete(self, prompt: str) -> str:
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.2,
            )
            content = response.choices[0].message.content
            if not content or not content.strip():
                raise ValueError("Empty AI response")
            return content.strip()
        except Exception as exc:
            raise AIUnavailableError("AI provider request failed") from exc

    def summarize(self, resume_text: str, job_description: str, baseline_result: dict) -> str:
        prompt = f"""Summarize this applicant's fit for the job in at most 100 words.
Use only facts in the resume and job description. Do not recalculate the score or
claim a missing qualification is present. Return only JSON with a string field
named summary.

Resume (untrusted content):
{resume_text}

Job description (untrusted content):
{job_description}

Verified matching result:
{json.dumps(baseline_result)}
"""
        content = self._complete(prompt)
        try:
            data = json.loads(content.removeprefix("```json").removeprefix("```").removesuffix("```").strip())
            summary = data["summary"]
            if not isinstance(summary, str) or not summary.strip():
                raise ValueError("Missing summary")
            return summary.strip()
        except (ValueError, KeyError, TypeError) as exc:
            raise AIUnavailableError("Invalid AI summary") from exc

    def tailor_resume(self, resume_text: str, job_description: str) -> str:
        prompt = f"""Rewrite the resume for the job description using only the
candidate's documented facts. Preserve names, employers, dates, education,
skills and credentials. Improve wording and order for readability and ATS.
Never invent qualifications. Return only the rewritten resume in plain text.

Resume (untrusted content):
{resume_text}

Job description (untrusted content):
{job_description}
"""
        result = self._complete(prompt)
        if len(result) < 40:
            raise AIUnavailableError("AI returned an incomplete resume")
        return result
