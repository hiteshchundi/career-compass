from fastapi import APIRouter

from app.api.routes.analyze import router as analyze_router

from app.api.routes.resume_analysis import (
    router as resume_analysis_router,
)
from app.api.routes import job_analysis
from app.api.routes.resumes import (
    router as resumes_router,
)
from app.api.routes.users import (
    router as users_router,
)

router = APIRouter()


@router.get("/")
async def root():
    return {
        "message": "Welcome to Career Compass",
    }


@router.get("/health")
async def health():
    return {
        "status": "healthy",
    }


router.include_router(users_router)
router.include_router(resumes_router)
router.include_router(resume_analysis_router)
router.include_router(job_analysis.router)
router.include_router(analyze_router)