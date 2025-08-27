from fastapi import FastAPI
from routers import MathAPI

app = FastAPI(
    title="My Awesome App",
    description="This is a very cool app with a modular structure.",
    version="1.0.0",
)

# Include the router from the math module
app.include_router(MathAPI.router, prefix="/math", tags=["Math Operations"])

@app.get("/")
async def root():
    """A simple root endpoint to confirm the app is running."""
    return {"message": "Hello World! Welcome to the main application."}