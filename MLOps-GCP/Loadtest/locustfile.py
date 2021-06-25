import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    #wait_time = between(1, 2.5)

    @task
    def submitForm(self):
        self.client.post("/predict", {"YearsExperience":"1"})
