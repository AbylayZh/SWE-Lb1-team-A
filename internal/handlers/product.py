from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from internal.service.product.product import ProductService

router = APIRouter()


@router.get("/products")
def get_all_products(db: Session = Depends(get_db)):
    service = ProductService(db)
    return service.get_all_products()


@router.get("/products/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):
    service = ProductService(db)
    return service.get_product_by_id(product_id)


@router.post("/products")
def create_product(product_data: dict, db: Session = Depends(get_db)):
    service = ProductService(db)
    return service.create_product(product_data)


@router.put("/products/{product_id}")
def update_product(product_id: int, product_data: dict, db: Session = Depends(get_db)):
    service = ProductService(db)
    return service.update_product(product_id, product_data)


@router.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    service = ProductService(db)
    return service.delete_product(product_id)
