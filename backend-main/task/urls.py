from task.entrypoint.routes import urlpatterns as task_url_patterns

app_name = "task"

urlpatterns = []

urlpatterns += task_url_patterns
