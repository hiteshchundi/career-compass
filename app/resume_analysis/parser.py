from app.schemas.resume_analysis import ResumeAnalysis
from app.resume_analysis.extractors import (
    extract_contact,
    extract_skills,
    extract_education,
    extract_experience,
    extract_projects,
    extract_certifications,
)


class ResumeParser:
    def parse(self, text: str) -> ResumeAnalysis:
        return ResumeAnalysis(
            contact=extract_contact(text),
            skills=extract_skills(text),
            education=extract_education(text),
            experience=extract_experience(text),
            projects=extract_projects(text),
            certifications=extract_certifications(text),
        )