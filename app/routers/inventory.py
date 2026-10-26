from fastapi import APIRouter

from app.schemas.inventory import InventoryBase

router = APIRouter(
    prefix="/inventory",
    tags=["inventory"],
)

@router.get("/")
def get_inventory():
    return []

@router.post("/")
def create_inventory_item(item: InventoryBase):
    return item

@router.put("/{item_id}")
def update_inventory_item(item_id: int, item: InventoryBase):
    return {
        "id": item_id,
        "item": item
    }

@router.delete("/{item_id}")
def delete_inventory_item(item_id: int):
    return {"id": item_id}