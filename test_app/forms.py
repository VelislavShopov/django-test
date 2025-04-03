from django import forms

from forms_test.models import Person
from test_app.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'