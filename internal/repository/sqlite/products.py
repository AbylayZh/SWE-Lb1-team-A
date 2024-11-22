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
            product = self.db.query(Product).filter(Product.id == product_id).first()
            if product:
                return product
            else:
                raise NotFoundError()
        except Exception as e:
            self.db.rollback()
            raise e

    def ReadAll(self):
        try:
            return self.db.query(Product).all()
        except Exception as e:
            self.db.rollback()
            raise e

    def Create(self, farmer_id: int, name: str, description: str, price: int, category_id: int, quantity: int,
               weight: float):
        try:
            product = Product(
                farmer_id=farmer_id,
                name=name,
                description=description,
                price=price,
                category_id=category_id,
                quantity=quantity,
                weight=weight,
            )
            self.db.add(product)
            # self.db.commit()
            self.db.flush()

            return product.id
        except Exception as e:
            self.db.rollback()
            raise e

    def Delete(self, product_id: int):
        try:
            product = self.Read(product_id)
            self.db.delete(product)  # Mark the user for deletion
            self.db.commit()  # Commit to apply the deletion
        except Exception as e:
            self.db.rollback()
            raise e
