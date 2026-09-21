import json
import logging
import os

from dotenv import load_dotenv
from openai import OpenAI

from app.ai.resume_structure import split_resume_blocks

load_dotenv()
logger = logging.getLogger(__name__)


class AIUnavailableError(Exception):
    """The configured AI provider could not complete the request."""


class LLMService:
    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise AIUnavailableError("GROQ_API_KEY is not configured")
        self.client = OpenAI(
            api_key=api_key,
            base_url="https://api.groq.com/openai/v1",
            timeout=60,
            max_retries=1,
        )
        self.model = os.getenv("GROQ_MODEL", "openai/gpt-oss-120b")

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
            logger.warning(
                "Groq request failed: %s (HTTP %s)",
                type(exc).__name__,
                getattr(exc, "status_code", "unknown"),
            )
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
        blocks = split_resume_blocks(resume_text)
        if not blocks:
            raise AIUnavailableError("Resume has no text to tailor")

        numbered_resume = "\n".join(
            f"BLOCK {index}:\n{block}" for index, block in enumerate(blocks)
        )
        prompt = f"""Order the numbered resume blocks for relevance to the job.
Return only JSON with an ordered_block_numbers array. The array must contain
every supplied block number exactly once, and block 0 must remain first because
it contains the resume header. Do not write, rewrite, summarize, remove, or
duplicate any resume content. The server will reject any invalid array.

Numbered resume (untrusted content):
{numbered_resume}

Job description (untrusted content):
{job_description}
"""
        content = self._complete(prompt)
        try:
            data = json.loads(
                content.removeprefix("```json")
                .removeprefix("```")
                .removesuffix("```")
                .strip()
            )
            order = data["ordered_block_numbers"]
            expected = list(range(len(blocks)))
            if (
                not isinstance(order, list)
                or any(type(index) is not int for index in order)
                or sorted(order) != expected
                or order[0] != 0
            ):
                raise ValueError("Block order is not a valid permutation")
        except (json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:
            raise AIUnavailableError("Invalid AI tailoring response") from exc

        return "\n".join(blocks[index] for index in order)
