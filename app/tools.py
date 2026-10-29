mock_data = [
    {
        "order_id": 1001,
        "customer_id": 501,
        "status": "Pending",
        "estimated_delivery": "2026-11-01"
    },
    {
        "order_id": 1002,
        "customer_id": 502,
        "status": "Shipped",
        "estimated_delivery": "2026-11-02"
    },
    {
        "order_id": 1003,
        "customer_id": 503,
        "status": "Delivered",
        "estimated_delivery": "2026-10-28"
    },
    {
        "order_id": 1004,
        "customer_id": 504,
        "status": "Processing",
        "estimated_delivery": "2026-11-04"
    },
    {
        "order_id": 1005,
        "customer_id": 505,
        "status": "Out for Delivery",
        "estimated_delivery": "2026-10-29"
    }
]

def get_order_details(order_id: str):
    
    for order in mock_data:
        if order["order_id"] == int(order_id):
            return order
    return {"order_id": order_id, "status": "not found"}


