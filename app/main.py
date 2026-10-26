from fastapi import FastAPI

from app.routers.inventory import router as inventory_router

app = FastAPI()

app.include_router(inventory_router)


@app.get("/")
def root():
    return {"message": "Backend is running"}