from django.urls import path
from auctions import views

urlpatterns = [
    path('test/', views.TestView.as_view(), name='test'),
]
