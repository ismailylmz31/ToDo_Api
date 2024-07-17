from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', views.register),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', views.user_logout),
    path('todos/', views.todo_list),
    path('todos/create/', views.todo_create),
    path('todos/<int:pk>/', views.todo_detail),
    path('todos/update/<int:pk>/', views.todo_update),
    path('todos/delete/<int:pk>/', views.todo_delete),
]
