from internal.repository.sqlite.products import ProductRepository
from internal.validators.products import ProductRequest


class ProductService:
    def __init__(self, db):
        self.product_repository = ProductRepository(db)

    def GetAllByFarmerID(self, farmer_id: int):
        try:
            return self.product_repository.ReadAllByFarmerID(farmer_id)
        except Exception as e:
            raise e

    def Get(self, product_id: int):
        return self.product_repository.Read(product_id)

    def Create(self, farmer_id: int, product_data: ProductRequest):
        try:
            return self.product_repository.Create(farmer_id, product_data.dict())
        except Exception as e:
            raise e

    def update_product(self, product_id: int, product_data: dict):
        return self.repository.update(product_id, product_data)

    def Delete(self, product_id: int):
        try:
            self.product_repository.Delete(product_id)
        except Exception as e:
            raise e
