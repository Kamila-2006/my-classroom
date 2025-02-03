from django.urls import path
from . import views


app_name = 'courses'

urlpatterns = [
    path('courses-list/', views.CourseListView.as_view(), name='list'),
    path('course-create/', views.CourseCreateView.as_view(), name='create'),
]