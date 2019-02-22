from django.urls import path
from auctions import views

app_name = 'auctions'
urlpatterns = [
    path('ads/', views.AdsListCreateView.as_view(), name='ads'),
    path('ads/<int:pk>/', views.AdsDetailView.as_view(), name='ads-detail'),
    path('ads/<int:pk>/bid/', views.BidCreateView.as_view(), name='bid'),
]


