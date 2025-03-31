from locust import HttpUser, task

class APITestUser(HttpUser):
    @task
    def test_add(self):
        self.client.get("/add/5/3")

    @task
    def test_multiply(self):
        self.client.get("/multiply/4/2")
