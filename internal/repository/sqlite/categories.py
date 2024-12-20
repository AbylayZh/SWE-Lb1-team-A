from sqlalchemy.orm import Session

from internal.repository.models.categories import Category


class CategoryRepository:
    def __init__(self, session: Session):
        self.db = session

    def ReadAll(self):
        try:
            return self.db.query(Category).all()
        except Exception as e:
            self.db.rollback()
            raise e
