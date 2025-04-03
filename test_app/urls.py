from django.urls import path

from test_app import views

urlpatterns = [
    path(r'', views.IndexView.as_view(), name='home'),
    path(r'users/', views.UserListView.as_view(),name='users'),
    path(r'users/form/', views.UserFormView.as_view(), name='form'),
    path(r'users/<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),
]