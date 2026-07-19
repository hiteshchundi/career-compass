from fastapi import FastAPI

from app.api.routers.resumes import router as resumes_router
from app.api.routers.users import router as users_router

app = FastAPI(
    title="Career Compass API",
    version="1.0.0",
)

app.include_router(users_router)
app.include_router(resumes_router)


@app.get("/", tags=["System"])
def root():
    return {
        "message": "Career Compass API is running!",
    }


@app.get("/health", tags=["System"])
def health():
    return {
        "status": "healthy",
    }