import pytest

from events.model import Event, EventStatus, DEAFULT_ORGANIZER
from events.errors import InvalidOrganizerError, InvalidTranstionStatus

from datetime import datetime

@pytest.fixture(scope="function")
def event():
    print("FIXTURE setuping!")
    
    yield Event(
        name="Tallinn Meeting",
        description="Meeting friends in Tallinn",
        place="Livalia, 23",
        date=datetime.today().weekday()
    )

    print("FIXTURE teardown!")

def test_create_event(event):
    assert event.name == "Tallinn Meeting"
    assert event.description == "Meeting friends in Tallinn"
    assert event.place == "Livalia, 23"
    assert event.date == datetime.today().weekday()
    assert event.organizer == DEAFULT_ORGANIZER
    assert event.status == EventStatus.DRAFT

def test_create_event_with_published_status():
    event = Event(
        name="Tallinn Meeting",
        description="Meeting friends in Tallinn",
        place="Livalia, 23",
        date=datetime.today().weekday(),
        status=EventStatus.PUBLISHED
    )

    assert event.status == EventStatus.PUBLISHED

def test_create_event_on_monday():
    with pytest.raises(ValueError):
        Event(
            name="Tallinn Meeting",
            description="Meeting friends in Tallinn",
            place="Livalia, 23",
            date=0
        )

def test_create_event_with_organizer_without_required_fields():
    with pytest.raises(InvalidOrganizerError):
        Event(
                name="Tallinn Meeting",
                description="Meeting friends in Tallinn",
                place="Livalia, 23",
                date=datetime.today().weekday(),
                organizer={
                    "wrongkey1":"data",
                    "wrongkey2":"data2"
                }
            )

def test_change_from_draft_to_finished():
    event = Event(
        name="Tallinn Meeting",
        description="Meeting friends in Tallinn",
        place="Livalia, 23",
        date=datetime.today().weekday()
    )

    with pytest.raises(InvalidTranstionStatus):
        event.change_status_to(EventStatus.FINISHED)

    assert event.status == EventStatus.DRAFT


@pytest.mark.parametrize(
    "from_status,to_status,expected",
    [
        # success
        (EventStatus.DRAFT, EventStatus.PUBLISHED, EventStatus.PUBLISHED),
        (EventStatus.PUBLISHED, EventStatus.CANCELED, EventStatus.CANCELED),
        (EventStatus.PUBLISHED, EventStatus.FINISHED, EventStatus.FINISHED),

        # fails
        (EventStatus.PUBLISHED, EventStatus.DRAFT, InvalidTranstionStatus),
    ]
)
def test_change_from_status1_to_status2_success(from_status,to_status,expected):
    
    # given
    event = Event(
        name="Tallinn Meeting",
        description="Meeting friends in Tallinn",
        place="Livalia, 23",
        date=datetime.today().weekday(),
        status=from_status
    )

    if type(expected) == type:
        # when
        with pytest.raises(expected):
            event.change_status_to(to_status)
    else:

        # when
        event.change_status_to(to_status)

        # assert
        assert event.status == expected


@pytest.mark.parametrize(
    "from_status,to_status,expected_exception",
    [
        (EventStatus.PUBLISHED, EventStatus.DRAFT, InvalidTranstionStatus),
        (EventStatus.PUBLISHED, EventStatus.DRAFT, InvalidTranstionStatus),
    ]
)
def test_change_from_status1_to_status2_unsuccess(from_status,to_status,expected_exception):
    
    # given
    event = Event(
        name="Tallinn Meeting",
        description="Meeting friends in Tallinn",
        place="Livalia, 23",
        date=datetime.today().weekday(),
        status=from_status
    )

    # when
    with pytest.raises(expected_exception):
        event.change_status_to(to_status)

def test_is_possible_day():
    assert Event.is_possible_day(0) == False