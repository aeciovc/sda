
from events.dao import DB
from events.model import Event
from events.upload import UploadImageService


class EventController:
    
    db = DB()
    upload_service = UploadImageService()

    def create(self, data):

        event = self._translate_from_dict(data)

        if event is None:
            return False

        try:
            self.db.insert("events", event)
        except:
            return (False, ConnectionError)
        
        try:
            self.upload_service.upload_from_url(event.picture)
        except Exception as e:
            return (False, ConnectionRefusedError)

        return True

    def _translate_from_dict(self, data):

        if data['day'] == "Saturday":
            data['date'] = 5

        return Event(**data)