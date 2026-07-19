from fastapi import APIRouter

from app.api.routes.resumes import router as resumes_router
from app.api.routes.users import router as users_router
# from app.api.routes.jobs import router as jobs_router
# from app.api.routes.analyses import router as analyses_router

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

# Enable these as you implement them.
# router.include_router(jobs_router)
# router.include_router(analyses_router)