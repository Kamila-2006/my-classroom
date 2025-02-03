from django.urls import path
from . import views


app_name = 'users'

urlpatterns = [
    path('users-list/', views.UsersListView.as_view(), name='list'),
    path('user-create/', views.UserCreateView.as_view(), name='create'),
]