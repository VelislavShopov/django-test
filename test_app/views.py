from django.shortcuts import render, redirect

from test_app.forms import UserForm
from test_app.models import User


# Create your views here.


def index_view(request):
    return render(request, 'test_app/index.html')


def users_view(request):
    users = User.objects.all()
    return render(request, 'test_app/users.html', {'users': users})


def form_view(request):

    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('users')

    form = UserForm()

    return render(request, 'test_app/users_form.html', {'form': form})