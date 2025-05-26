from locust import HttpUser, task, between

class FooBarUser(HttpUser):
    wait_time = between(0, 1)

    @task
    def foo(self):
        self.client.get("/", headers={"Host": "foo.localhost"}, name="GET / (foo)")

    @task
    def bar(self):
        self.client.get("/", headers={"Host": "bar.localhost"}, name="GET / (bar)")
