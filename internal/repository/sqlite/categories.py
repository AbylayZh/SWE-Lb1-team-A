from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from internal.repository.models.categories import Category


class CategoryRepository:
    def __init__(self, session: Session):
        self.session = session

    def add_category(self, name: str) -> Category:
        """Adds a new category to the database."""
        new_category = Category(name=name)
        try:
            self.session.add(new_category)
            self.session.commit()
            return new_category
        except SQLAlchemyError as e:
            self.session.rollback()
            print(f"Error adding category: {e}")
            return None

    def get_category_by_id(self, category_id: int) -> Category:
        """Fetches a category by its ID."""
        return self.session.query(Category).filter_by(id=category_id).first()

    def get_all_categories(self) -> list:
        """Retrieves all categories."""
        return self.session.query(Category).all()

    def update_category(self, category_id: int, name: str) -> bool:
        """Updates the name of an existing category."""
        category = self.get_category_by_id(category_id)
        if category:
            category.name = name
            try:
                self.session.commit()
                return True
            except SQLAlchemyError as e:
                self.session.rollback()
                print(f"Error updating category: {e}")
                return False
        return False

    def delete_category(self, category_id: int) -> bool:
        """Deletes a category by its ID."""
        category = self.get_category_by_id(category_id)
        if category:
            try:
                self.session.delete(category)
                self.session.commit()
                return True
            except SQLAlchemyError as e:
                self.session.rollback()
                print(f"Error deleting category: {e}")
                return False
        return False
