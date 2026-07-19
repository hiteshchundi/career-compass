from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ResumeRead(BaseModel):
    """
    Response schema for a stored resume.
    """

    id: int
    user_id: int

    original_filename: str
    stored_filename: str

    file_path: str
    file_type: str

    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True,
    )