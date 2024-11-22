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

    def GetAll(self):
        try:
            return self.product_repository.ReadAll()
        except Exception as e:
            raise e

    def Get(self, product_id: int):
        try:
            return self.product_repository.Read(product_id)
        except Exception as e:
            raise e

    def Create(self, farmer_id: int, product_data: ProductRequest):
        try:
            name, description, price, category_id, quantity, weight = product_data.name, product_data.description, product_data.price, product_data.category_id, product_data.quantity, product_data.weight
            return self.product_repository.Create(farmer_id, name.capitalize(), description.capitalize(), price,
                                                  category_id, quantity, weight)
        except Exception as e:
            raise e

    def Delete(self, product_id: int):
        try:
            self.product_repository.Delete(product_id)
        except Exception as e:
            raise e
