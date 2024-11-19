from internal.repository.sqlite.ProductRepository import ProductRepository

class ProductService:
    def __init__(self, db):
        self.repository = ProductRepository(db)

    def get_all_products(self):
        return self.repository.get_all()

    def get_product_by_id(self, product_id: int):
        return self.repository.get_by_id(product_id)

    def create_product(self, product_data: dict):
        return self.repository.create(product_data)

    def update_product(self, product_id: int, product_data: dict):
        return self.repository.update(product_id, product_data)

    def delete_product(self, product_id: int):
        return self.repository.delete(product_id)
