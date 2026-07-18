from pydantic import BaseModel, ConfigDict


class AnalysisCreate(BaseModel):
    resume_id: int
    job_id: int
    score: float
    feedback: str


class AnalysisRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    resume_id: int
    job_id: int
    score: float
    feedback: str