import os
from typing import List

from fastapi import UploadFile

from internal.repository.sqlite.images import ImageRepository


class ImageService:
    def __init__(self, db):
        self.image_repository = ImageRepository(db)

    def GetAllByProductID(self, product_id: int):
        return self.image_repository.ReadAllByProductID(product_id)

    def Upload(self, product_id: int, path: str):
        self.image_repository.Create(product_id, path)

    async def UploadMultiple(self, product_id: int, files: List[UploadFile]):
        for file in files:
            file_location = f"/uploaded_images/product_id_{product_id}/{file.filename}"
            os.makedirs(os.path.dirname(file_location), exist_ok=True)

            with open(file_location, "wb") as f:
                f.write(await file.read())

            self.Upload(product_id, file_location)
