from events.controller import EventController

from unittest.mock import Mock

# Controller Layer
class TestCreateEventControllerInt:

    # success
    def test_create_event(self, event):
        event_controller = EventController()
        
        # Mocking upload inside EventController
        event_controller.upload_service = Mock()
        
        result = event_controller.create(event)
        assert result is True