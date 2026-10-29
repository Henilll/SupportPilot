
import logging
import re

from fastapi import FastAPI, HTTPException

from agent import get_support_response
from schema import ChatRequest, SupportResponse

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Customer Support API")


@app.get("/")
def home():
    return {"message": "Customer Support API is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/chat", response_model=SupportResponse)
def chat(request: ChatRequest):
    try:
        answer = get_support_response(
            customer_id=request.customer_id,
            message=request.message,
        )

        match = re.search(
            r"\b(\d{4,})\b",
            request.message,
        )

        return SupportResponse(
            status="success",
            answer=answer,
            order_id=match.group(1) if match else None,
            ticket_id=None,
        )

    except Exception as exc:
        logger.exception("Error processing customer support request")

        # Show details during local development only.
        raise HTTPException(
            status_code=502,
            detail=f"Support agent failed: {str(exc)}",
        ) from exc
