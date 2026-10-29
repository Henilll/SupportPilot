from fastapi import FastAPI

from tools import get_order_details
from schema import ChatRequest, SupportResponse
app=FastAPI()

@app.get("/health")
def check_health():
    return {"status": "healthy"}


@app.post("/support/chat",response_model=SupportResponse)
def chat_support(request: ChatRequest):
    customer_id = request.customer_id
    message = request.message

    if not customer_id or not message:
        return {"status": "error", "answer": "Missing customer_id or message"}

    # Simulate a support response based on the message
    if "order" in message.lower():
        order_id = message.split()[-1]  # Assume the last word is the order ID
        order_details = get_order_details(order_id)
        if order_details["status"] == "not found":
            return {"status": "error", "answer": f"Order {order_id} not found"}
        else:
            return {
                "status": "success",
                "answer": f"Your order {order_id} is currently {order_details['status']}. Estimated delivery: {order_details['estimated_delivery']}",
                "order_id": order_id
            }
    else:
        return {"status": "success", "answer": "Thank you for reaching out. How can we assist you further?"}
# declare Declare SupportResponse as the response model.
