from locust import HttpLocust, TaskSet, task

class WebsiteTasks(TaskSet):
   @task
   def search(self):
      self.client.get("/stuff")
      
class WebsiteUser(HttpLocust):
   task_set = WebsiteTasks