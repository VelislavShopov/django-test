from django import forms

class FormTest(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 18:
            raise forms.ValidationError('age is too young')

    def clean_name(self):
        name = self.cleaned_data['name']
        if name != '':
            raise forms.ValidationError('name is already taken')






