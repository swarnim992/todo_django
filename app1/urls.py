from django.urls import path
from .views import calculate, demo_json, home, todo_list, todo_create, todo_update, todo_delete

urlpatterns = [
    path('home/', home, name='home'),
    path('demo_json/', demo_json, name='demo_json'),
    path('todos/', todo_list, name='todo_list'),
    path('todos/create/', todo_create, name='todo_create'),
    path('todos/<int:pk>/update/', todo_update, name='todo_update'),
    path('todos/<int:pk>/delete/', todo_delete, name='todo_delete'),
    path('calculate/', calculate, name='calculate'),
]
