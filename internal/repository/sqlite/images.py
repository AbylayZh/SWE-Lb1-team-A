from sqlalchemy.orm import Session

from internal.repository.models.images import Image  # Adjust path if needed


class ImageRepository:
    def __init__(self, db: Session):
        self.db = db

    def ReadAllByProductID(self, product_id: int):
        try:
            return self.db.query(Image).filter(Image.product_id == product_id).all()
        except Exception as e:
            self.db.rollback()
            raise e

    def Create(self, product_id: int, path: str):
        try:
            image = Image(product_id=product_id, path=path)
            self.db.add(image)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e
