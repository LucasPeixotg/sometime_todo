from django.urls import path
from .views import task_index, task_create, task_delete, task_check

app_name = "tasks"
urlpatterns = [
    path('', task_index, name='task_index'),
    path('create/', task_create, name='task_create'),
    path('<int:task_id>/delete', task_delete, name='task_delete'),
    path('<int:task_id>/check', task_check, name='task_check'),
]
