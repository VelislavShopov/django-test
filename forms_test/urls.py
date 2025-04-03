from django.urls import path

from forms_test import views

urlpatterns = [
    path('form/',views.PersonCreateView.as_view(),name='form'),
]