from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, FormView, CreateView

from test_app.forms import UserForm
from test_app.models import User


# Create your views here.


class IndexView(View):
    template_name = 'test_app/index.html'
    def get(self, request):
        return render(request, self.template_name)


class UserListView(ListView):
    model = User
    template_name = 'test_app/users.html'

class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'test_app/users_form.html'

