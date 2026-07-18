from pydantic import BaseModel, ConfigDict


class ResumeCreate(BaseModel):
    user_id: int
    filename: str
    content: str


class ResumeRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    filename: str
    content: str