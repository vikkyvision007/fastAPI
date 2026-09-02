from fastapi import FastAPI 
from fastapi import Request
import uvicorn

app = FastAPI(
    title="Swiggy Order Service",
    description="This is a sample FastAPI application for Swiggy Order Service",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc", 
    openapi_url="/openapi.json"
)

@app.get("/")
def read_root():
    """ Root endpoint to check the health of the service. """
    return {
            "message": "Welcome to the world of Swiggy Order Service",
            "Status": "Healthy Service"
            }

@app.get("/about")
def about():
    """ Return API Metadata """
    return {
            "service": "Order Service",
            "team": "Backend Platform Team",
            "region": "ap-south-1",
            "version": "1.0.0",
            }

@app.get("/orders")
def list_orders():
    """ List all orders """
    return {
            "orders": [
                {"order_id": 1, "item": "Pizza", "quantity": 2},
                {"order_id": 2, "item": "Burger", "quantity": 1},
                {"order_id": 3, "item": "Pasta", "quantity": 3}
            ]
        }   

@app.get("/orders/status")
def order_status(order_id: int):
    """ Get the status of a specific order by order_id """
    # In a real application, you would fetch this from a database
    order_status_map = {
        1: "Delivered",
        2: "In Transit",
        3: "Preparing"
    }
    status = order_status_map.get(order_id, "Order not found")
    return {
        "order_id": order_id,
        "status": status
    }

@app.get("/debug/request-info")
async def request_info(request: Request):
    """ Debug endpoint to display request information """
    return {
        "method": request.method,
        "url": str(request.url),
        "headers": dict(request.headers),
        "path_params": request.path_params,
        "query_params": dict(request.query_params)
    }

@app.get(
    "/orders/active",
    summary="Get active orders",
    description=("This endpoint returns a list of active orders for the user."),
    tags=["Orders"],
    response_description="A list of active orders",
    deprecated=False
    )
def active_orders():
    """ Get a list of active orders, This appears in docs"""
    return {
        "active_orders": [
            {"order_id": 1, "item": "Pizza", "quantity": 2, "status": "In Transit"},
            {"order_id": 3, "item": "Pasta", "quantity": 3, "status": "Preparing"}
        ]
    }

@app.get("/resturants",
         summary="Get list of resturants",
         description=("This endpoint returns a list of resturants for the user."),
         response_description="A list of resturants",
         tags=["Resturants"],
         deprecated=False
         )
def list_resturants():
    """ Get a list of resturants, This appears in docs"""
    return {
        "resturants": [
            {"resturant_id": 1, "name": "Pizza Palace", "cuisine": "Italian"},
            {"resturant_id": 2, "name": "Burger Barn", "cuisine": "American"},
            {"resturant_id": 3, "name": "Pasta Paradise", "cuisine": "Italian"}
        ]
    }