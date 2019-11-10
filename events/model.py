
from events.errors import InvalidOrganizerError, InvalidTranstionStatus

DEAFULT_ORGANIZER = {
    "name": "John",
    "email": "john@tallin.com",
    "phone_number": "533 444 222"
}

class EventStatus:
    DRAFT = 'draft'
    PUBLISHED = 'published'
    CANCELED = 'canceled'
    FINISHED = 'finished'

class Event:

    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.description = kwargs['description']
        self.place = kwargs['place']
        self.date = self._get_valid_date(kwargs['date'])
        self.organizer = self._get_valid_organizer(kwargs.get('organizer', DEAFULT_ORGANIZER))
        self.status = kwargs.get('status', EventStatus.DRAFT)
        self.picture = kwargs.get('picture', 'https://www.traveller.ee/blog/wp-content/uploads/2013/10/12344348133_95f14f8a31_k-680x450.jpg')

    @classmethod
    def is_possible_day(cls, day):
        return False if day >= 0  and day <= 4 else True 

    def _get_valid_date(self, date):
        if date >= 0  and date <= 4:
            raise ValueError("Only Saturdays and Sundays are allowed!")
        return date

    def _get_valid_organizer(self, organizer):
        try:
            return {
                'name': organizer['name'],
                'phone_number': organizer['phone_number'],
                'email': organizer['email']
            }
        except:
            raise InvalidOrganizerError()

    def change_status_to(self, new_status):
        if self.status == EventStatus.DRAFT:
            if new_status == EventStatus.PUBLISHED:
                self.status = new_status
                return
        elif self.status == EventStatus.PUBLISHED:
            if new_status == EventStatus.FINISHED or new_status == EventStatus.CANCELED:
                self.status = new_status
                return

        raise InvalidTranstionStatus()


class User:
    pass

