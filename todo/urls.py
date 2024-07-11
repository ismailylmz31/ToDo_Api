from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ToDoCreate, ToDoDelete, ToDoDetail, ToDoList, ToDoUpdate, ToDoViewSet,  PhotoViewSet

router = DefaultRouter()
router.register(r'todos/viewset', ToDoViewSet)
router.register(r'photos', PhotoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('todos/', ToDoList.as_view(), name='todo-list'),
    path('todos/create/', ToDoCreate.as_view(), name='todo-create'),
    path('todos/<int:pk>/', ToDoDetail.as_view(), name='todo-detail'),
    path('todos/update/<int:pk>/', ToDoUpdate.as_view(), name='todo-update'),
    path('todos/delete/<int:pk>/', ToDoDelete.as_view(), name='todo-delete'),
    
]

