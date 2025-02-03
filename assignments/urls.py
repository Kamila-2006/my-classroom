from django.urls import path
from . import views


app_name = 'assignments'

urlpatterns = [
    path('assignments-list/', views.AssignmentListView.as_view(), name='list'),
    path('assignment-create/', views.AssignmentCreateView.as_view(), name='create'),
]