from django.urls import path

from test_app import views

urlpatterns = [
    path(r'', views.index_view, name='home'),
    path(r'users/', views.users_view,name='users'),
    path(r'users/form/', views.form_view, name='form'),
]