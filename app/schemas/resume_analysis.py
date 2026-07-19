from pydantic import BaseModel


class ContactInfo(BaseModel):
    name: str | None = None
    email: str | None = None
    phone: str | None = None
    location: str | None = None
    linkedin: str | None = None
    github: str | None = None


class Education(BaseModel):
    institution: str
    degree: str | None = None
    graduation_year: str | None = None


class Experience(BaseModel):
    company: str
    title: str | None = None
    duration: str | None = None
    description: str | None = None


class Project(BaseModel):
    name: str
    description: str | None = None


class Certification(BaseModel):
    name: str


class ResumeAnalysis(BaseModel):
    contact: ContactInfo

    skills: list[str] = []

    education: list[Education] = []

    experience: list[Experience] = []

    projects: list[Project] = []

    certifications: list[Certification] = []