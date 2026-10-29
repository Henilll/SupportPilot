
from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    customer_id: str = Field(..., min_length=1)
    message: str = Field(..., min_length=1)


class SupportResponse(BaseModel):
    status: str
    answer: str
    order_id: str | None = None
    ticket_id: str | None = None
