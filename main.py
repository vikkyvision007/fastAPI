from fastapi import FastAPI

app = FastAPI()     

@app.get("/")
def read_root():
    return {
            "message": "Welcome to the world of Swiggy Order Service",
            "Status": "Healthy Service is up and running",
            "Version": "1.0.0",
            }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)