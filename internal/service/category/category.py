from typing import List, Optional

from internal.repository.models.categories import Category
from internal.repository.sqlite.categories import CategoryRepository


class CategoryService:
    def __init__(self, category_repository: CategoryRepository):
        self.category_repository = category_repository

    def create_category(self, name: str) -> Optional[Category]:
        """Creates a new category with the given name."""
        if not name:
            print("Category name cannot be empty.")
            return None
        return self.category_repository.add_category(name)

    def get_category(self, category_id: int) -> Optional[Category]:
        """Retrieves a category by its ID."""
        category = self.category_repository.get_category_by_id(category_id)
        if not category:
            print(f"No category found with ID {category_id}.")
        return category

    def list_categories(self) -> List[Category]:
        """Lists all categories."""
        return self.category_repository.get_all_categories()

    def update_category(self, category_id: int, new_name: str) -> bool:
        """Updates the name of an existing category."""
        if not new_name:
            print("New category name cannot be empty.")
            return False
        return self.category_repository.update_category(category_id, new_name)

    def delete_category(self, category_id: int) -> bool:
        """Deletes a category by its ID."""
        category = self.get_category(category_id)
        if category:
            return self.category_repository.delete_category(category_id)
        print(f"Category with ID {category_id} does not exist.")
        return False
