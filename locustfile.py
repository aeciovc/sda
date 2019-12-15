from locust import HttpLocust, TaskSet, task


class TestEndpoints(TaskSet):
    @task
    def test_post_event(self):
        self.client.post("/event", data={
                "name":"Tallinn Meeting",
                "description":"Meeting friends in Tallinn",
                "place":"Livalia, 23",
                "day":"Saturday",
                "picture": "https://mypicture.com/png.png"
            }
        )

    @task
    def test_get_events(self):
        pass
        #TODO


class MyLocust(HttpLocust):
    task_set = TestEndpoints
