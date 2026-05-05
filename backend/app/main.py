from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.database import get_db

app = FastAPI(
    title="OutfitCheck-AI API",
    description="Backend API for OutfitCheck-AI: A digital stylist application.",
    version="0.1.0",
)

# Configure CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify the actual frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from app.routers import auth, wardrobe

app.include_router(auth.router)
app.include_router(wardrobe.router)

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Welcome to the OutfitCheck-AI API"}

@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    try:
        # Simple query to check database connection
        db.execute(text("SELECT 1"))
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        return {"status": "unhealthy", "database": "disconnected", "error": str(e)}
