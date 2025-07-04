from fastapi import FastAPI

app = FastAPI()

@app.get("/orders")
def read_orders():
    return [
        {"id": 1, "item": "Laptop"},
        {"id": 2, "item": "Mouse"}
    ]
@app.get("/orders/{order_id}")
def read_order(order_id: int):
    return {"id": order_id, "item": "Laptop"}

@app.get("/test")
def test():
    return {"test":"testing"}