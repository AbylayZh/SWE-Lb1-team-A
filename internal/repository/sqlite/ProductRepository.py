from sqlalchemy.orm import Session
from internal.repository.models.users import Product  # Adjust the import path if needed

class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        """Fetch all products from the database."""
        return self.db.query(Product).all()

    def get_by_id(self, product_id: int):
        """Fetch a single product by its ID."""
        return self.db.query(Product).filter(Product.id == product_id).first()

    def create(self, product_data: dict):
        """Insert a new product into the database."""
        product = Product(**product_data)
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product

    def update(self, product_id: int, product_data: dict):
        """Update an existing product by its ID."""
        product = self.get_by_id(product_id)
        if product:
            for key, value in product_data.items():
                setattr(product, key, value)
            self.db.commit()
            self.db.refresh(product)
        return product

    def delete(self, product_id: int):
        """Delete a product by its ID."""
        product = self.get_by_id(product_id)
        if product:
            self.db.delete(product)
            self.db.commit()
        return product
