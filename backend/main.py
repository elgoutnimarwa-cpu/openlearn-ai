from fastapi import FastAPI

app = FastAPI(
    title="OpenLearn AI",
    description="AI-powered learning platform",
    version="0.1.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to OpenLearn AI"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
