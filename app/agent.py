
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.agents import create_agent

from tools import get_order_details,cancel_order

load_dotenv()

if not os.getenv("GROQ_API_KEY"):
    raise RuntimeError("GROQ_API_KEY is missing from .env")

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0,
)

agent = create_agent(
    model=llm,
    tools=[get_order_details, cancel_order],
      system_prompt="""
    You are a helpful customer support assistant.

    Rules:
    1. Help customers with order-related questions.
    2. Use get_order_details when order information is needed.
    3. Always use the customer_id supplied in the request.
    4. Never invent order details or delivery dates.
    5. If an order is not found, explain this politely.
    6. Keep responses clear and concise.
    7. Do not claim to create support tickets.
    """,
)


def get_support_response(customer_id: str, message: str) -> str:
    """Run the support agent and return its final answer."""

    result = agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": (
                    f"Customer ID: {customer_id}\n"
                    f"Customer message: {message}"
                ),
            }
        ]
    })

    final_message = result["messages"][-1]
    content = final_message.content

    if isinstance(content, str):
        return content

    # Handle models that return structured content blocks.
    return "\n".join(
        block["text"]
        for block in content
        if isinstance(block, dict)
        and block.get("type") == "text"
    )
