from pydantic import BaseModel, ConfigDict


class JobCreate(BaseModel):
    title: str
    company: str
    description: str


class JobRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    company: str
    description: str    