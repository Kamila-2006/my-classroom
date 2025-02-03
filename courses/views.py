from django.shortcuts import render, redirect, get_object_or_404
from .models import Course
from django.views import View
from .forms import CourseForm


class CourseListView(View):
    def get(self, request):
        courses = Course.objects.all()
        ctx = {'courses':courses}
        return render(request, 'courses/courses.html', ctx)

class CourseCreateView(View):
    def get(self, request):
        form = CourseForm
        ctx = {'form':form}
        return render(request, 'courses/course-form.html', ctx)

    def post(self, request):
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses:list')