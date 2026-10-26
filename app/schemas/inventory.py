from pydantic import BaseModel

class InventoryBase(BaseModel):
    name: str
    quantity: float