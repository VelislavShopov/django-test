from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, FormView, CreateView, DetailView

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

# class UserCreateView(CreateView):
#     model = User
#     form_class = UserForm
#     template_name = 'test_app/users_form.html'

class UserFormView(FormView):
    form_class = UserForm
    template_name = 'test_app/users_form.html'
    success_url = '/help/users/'


    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class UserDetailView(DetailView):
    model = User
    template_name = 'test_app/user_detail.html'
    context_object_name = 'user'