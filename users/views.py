from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import User
from django.views import View
from .forms import UserForm


def home(request):
    return render(request, 'index.html')

class UsersListView(View):
    def get(self, request):
        users = User.objects.all()
        ctx = {'users':users}
        return render(request, 'users/users.html', ctx)

class UserCreateView(View):
    def get(self, request):
        form = UserForm()
        ctx = {'form':form}
        return render(request, 'users/users-form.html', ctx)

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('users:list'))
        ctx = {'form':form}
        return render(request, 'users/users-form.html', ctx)
