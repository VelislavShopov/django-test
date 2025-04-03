from django.shortcuts import render

from forms_test.forms import FormTest
from forms_test.models import Person


# Create your views here.
def form_view(request):
    if request.method == "POST":
        form = FormTest(request.POST)
        if form.is_valid():
            Person.objects.create(
                name=form.cleaned_data['name'],
                age=form.cleaned_data['age'],
            )
    else:
        form = FormTest()

    return render(request,'forms_test/form.html',{'form':form})