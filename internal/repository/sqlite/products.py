from sqlalchemy.orm import Session

from internal.repository.models.errors import NotFoundError
from internal.repository.models.products import Product  # Adjust the import path if needed


class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def ReadAllByFarmerID(self, farmer_id: int):
        try:
            return self.db.query(Product).filter(Product.farmer_id == farmer_id).all()
        except Exception as e:
            self.db.rollback()
            raise e

    def Read(self, product_id: int):
        try:
            return self.db.query(Product).filter(Product.id == product_id).first()
        except Exception as e:
            self.db.rollback()
            raise e

    def Create(self, farmer_id: int, product_data: dict):
        try:
            product_data['farmer_id'] = farmer_id
            product = Product(**product_data)
            self.db.add(product)
            self.db.commit()
            self.db.flush()

            return product.id
        except Exception as e:
            self.db.rollback()
            raise e

    def Delete(self, product_id: int):
        try:
            product = self.db.query(Product).filter(Product.id == product_id).first()
            if product:
                self.db.delete(product)  # Mark the user for deletion
                self.db.commit()  # Commit to apply the deletion
            else:
                raise NotFoundError()
        except Exception as e:
            self.db.rollback()
            raise e
