from pydantic import BaseModel


class ChatRequest(BaseModel):
    customer_id: str
    message: str

class SupportResponse(BaseModel):
    status: str
    answer: str
    order_id: str = None
    ticket_id: str = None

