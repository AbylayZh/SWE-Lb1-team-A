from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from internal.service.image.ImageService import ImageService
from pkg.dependencies import get_db

router = APIRouter()

@router.get("/images")
def get_all_images(db: Session = Depends(get_db)):
    service = ImageService(db)
    return service.get_all_images()

@router.post("/images")
def create_image(image_data: dict, db: Session = Depends(get_db)):
    service = ImageService(db)
    return service.create_image(image_data)

@router.put("/images/{image_id}")
def update_image(image_id: int, image_data: dict, db: Session = Depends(get_db)):
    service = ImageService(db)
    return service.update_image(image_id, image_data)

@router.delete("/images/{image_id}")
def delete_image(image_id: int, db: Session = Depends(get_db)):
    service = ImageService(db)
    return service.delete_image(image_id)
