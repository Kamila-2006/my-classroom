from django.shortcuts import render, redirect
from .models import Assignment
from django.views import View
from .forms import AssignmentForm


class AssignmentListView(View):
    def get(self, request):
        assignments = Assignment.objects.all()
        ctx = {'assignments':assignments}
        return render(request, 'assignments/assignments.html', ctx)

class AssignmentCreateView(View):
    def get(self, request):
        form = AssignmentForm
        ctx = {'form':form}
        return render(request, 'assignments/assignments-form.html', ctx)

    def post(self, request):
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('assignments:list')