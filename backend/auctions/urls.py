from django.urls import path
from auctions import views

urlpatterns = [
    path('ads/', views.AdsListCreateView.as_view(), name='ads'),
    path('ads/<int:pk>/', views.AdsDetailView.as_view(), name='ads-detail'),
]
