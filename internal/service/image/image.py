from internal.repository.sqlite.images import ImageRepository


class ImageService:
    def __init__(self, repository: ImageRepository):
        self.repository = repository

    def get_all_images(self):
        """Fetch all images."""
        return self.repository.get_all()

    def get_image_by_id(self, image_id: int):
        """Fetch an image by its ID."""
        return self.repository.get_by_id(image_id)

    def create_image(self, image_data: dict):
        """Create a new image."""
        return self.repository.create(image_data)

    def update_image(self, image_id: int, image_data: dict):
        """Update an existing image."""
        return self.repository.update(image_id, image_data)

    def delete_image(self, image_id: int):
        """Delete an image by its ID."""
        return self.repository.delete(image_id)
