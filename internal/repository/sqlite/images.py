from sqlalchemy.orm import Session

from internal.repository.models.images import Image  # Adjust path if needed


class ImageRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        """Fetch all images from the database."""
        return self.db.query(Image).all()

    def get_by_id(self, image_id: int):
        """Fetch a single image by its ID."""
        return self.db.query(Image).filter(Image.id == image_id).first()

    def create(self, image_data: dict):
        """Insert a new image into the database."""
        image = Image(**image_data)
        self.db.add(image)
        self.db.commit()
        self.db.refresh(image)
        return image

    def update(self, image_id: int, image_data: dict):
        """Update an existing image by its ID."""
        image = self.get_by_id(image_id)
        if image:
            for key, value in image_data.items():
                setattr(image, key, value)
            self.db.commit()
            self.db.refresh(image)
        return image

    def delete(self, image_id: int):
        """Delete an image by its ID."""
        image = self.get_by_id(image_id)
        if image:
            self.db.delete(image)
            self.db.commit()
        return image
