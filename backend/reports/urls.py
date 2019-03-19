from django.urls import path

from . import views

urlpatterns = [
    path('ads/<int:pk>/', views.AdsReportView.as_view(), name='ads-report'),
    path('users/<int:pk>/', views.UsersReportView.as_view(), name='user-report'),
]
