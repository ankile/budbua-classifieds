from django.urls import path
from users import views

urlpatterns = [
    path('users/', views.UsersListCreateView.as_view(), name='users'),
]
