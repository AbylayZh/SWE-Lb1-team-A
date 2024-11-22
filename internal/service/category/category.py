from typing import List

from sqlalchemy.orm import Session

from internal.repository.models.categories import Category
from internal.repository.sqlite.categories import CategoryRepository


class CategoryService:
    def __init__(self, db: Session):
        self.category_repository = CategoryRepository(db)

    def GetAll(self) -> List[Category]:
        try:
            return self.category_repository.ReadAll()
        except Exception as e:
            raise e
