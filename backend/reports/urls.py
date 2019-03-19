from django.urls import path

from . import views

urlpatterns = [
    path('ads/<int:pk>/', views.AdReportCreateView.as_view(), name='ads-report'),
    path('users/<int:pk>/', views.UserReportCreateView.as_view(), name='user-report'),
]
