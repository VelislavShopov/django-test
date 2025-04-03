from django.urls import path

from test_app import views

urlpatterns = [
    path(r'', views.IndexView.as_view(), name='home'),
    path(r'users/', views.UserListView.as_view(),name='users'),
    path(r'users/form/', views.UserCreateView.as_view(), name='form'),
]