from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status

from app.api.dependencies import get_resume_service
from app.schemas.resume import ResumeRead
from app.services.resume_service import ResumeService

router = APIRouter(
    prefix="/resumes",
    tags=["Resumes"],
)


@router.post(
    "",
    response_model=ResumeRead,
    status_code=status.HTTP_201_CREATED,
)
def upload_resume(
    user_id: int,
    file: UploadFile = File(...),
    service: ResumeService = Depends(get_resume_service),
) -> ResumeRead:
    """
    Upload a resume for a user.
    """

    return service.upload_resume(
        user_id=user_id,
        file=file,
    )


@router.get(
    "/{resume_id}",
    response_model=ResumeRead,
)
def get_resume(
    resume_id: int,
    service: ResumeService = Depends(get_resume_service),
) -> ResumeRead:
    """
    Retrieve a resume by ID.
    """

    resume = service.get_resume(resume_id)

    if resume is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Resume not found.",
        )

    return resume


@router.get(
    "/user/{user_id}",
    response_model=list[ResumeRead],
)
def list_user_resumes(
    user_id: int,
    service: ResumeService = Depends(get_resume_service),
) -> list[ResumeRead]:
    """
    List all resumes uploaded by a user.
    """

    return service.list_user_resumes(user_id)