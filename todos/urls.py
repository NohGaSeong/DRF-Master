from todos.views import TodoAPIView
from django.urls import path

urlpatterns = [
    # path('create', CreateTodoAPIView.as_view(), name = 'create-todo'),
    # path('list', TodoListAPIView.as_view(), name = 'list-todo')
    path("", TodoAPIView.as_view(), name = "todos")
]