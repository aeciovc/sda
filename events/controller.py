
from events.dao import DB


class EventController:
    
    db = DB()

    def create(self, event):
        self.db.insert("events", event)
        return True