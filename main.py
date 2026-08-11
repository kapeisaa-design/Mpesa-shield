from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from analyzer import analyze_message
from models import AnalyzeRequest


app = FastAPI(
    title="M-PESA Shield API",
    description=(
        "Educational API for identifying suspicious "
        "message indicators."
    ),
    version="1.0.0",
)


# Local development only.
# Production should use a specific trusted frontend origin.
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
    ],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)


@app.get("/health")
def health_check():
    """
    Check whether the API is running.
    """

    return {
        "status": "ok",
        "service": "M-PESA Shield API",
    }


@app.post("/analyze")
def analyze(request: AnalyzeRequest):
    """
    Analyze a submitted message.
    """

    try:

        result = analyze_message(
            request.message
        )

        return {
            "score": result.score,
            "category": result.category,
            "reasons": result.reasons,
            "recommendations": result.recommendations,
        }

    except ValueError as error:

        raise HTTPException(
            status_code=400,
            detail=str(error),
        )