from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ToDoViewSet, delete_multiple_todos, PhotoViewSet

router = DefaultRouter()
router.register(r'todos', ToDoViewSet)
router.register(r'photos', PhotoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('todos/delete_multiple/', delete_multiple_todos, name='delete_multiple_todos'),
]
