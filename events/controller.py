
from events.dao import DB
from events.upload import UploadImageService


class EventController:
    
    db = DB()
    upload_service = UploadImageService()

    def create(self, event):
        if event is None:
            return False

        self.db.insert("events", event)

        self.upload_service.upload_from_url(event.picture)

        return True