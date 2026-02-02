from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes import router as api_router
from src.config import settings

app = FastAPI(title="My FastAPI App", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(api_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to My FastAPI App!"}