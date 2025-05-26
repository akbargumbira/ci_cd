from locust import HttpUser, task, between

class FooBarUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def foo(self):
        self.client.get("/", headers={"Host": "foo.localhost"})

    @task
    def bar(self):
        self.client.get("/", headers={"Host": "bar.localhost"})
