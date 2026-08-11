from pydantic import BaseModel, Field


class AnalyzeRequest(BaseModel):
    """
    Request body accepted by the message-analysis API.
    """

    message: str = Field(
        ...,
        min_length=1,
        max_length=2000,
        description="Message to analyze.",
    )