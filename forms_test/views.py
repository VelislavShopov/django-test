from django.shortcuts import render
from django.views.generic import CreateView

from forms_test.forms import FormTest
from forms_test.models import Person


# Create your views here.

class PersonCreateView(CreateView):
    model = Person
    template_name = 'forms_test/form.html'
    fields = ['name','age']
    success_url = '/forms_test/form'
