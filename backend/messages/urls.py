from django.urls import path

from . import views

app_name = 'messages'
urlpatterns = [
    path('messages/', views.TestView.as_view(), name='messages'),
    path('messages/<int:pk>', views.TestView.as_view(), name='messages-chat'),

]

#path('ads/', views.AdsListCreateView.as_view(), name='ads'),
 #   path('ads/<int:pk>/', views.AdsDetailView.as_view(), name='ads-detail'),
    #path('ads/<int:pk>/bid/', views.BidCreateView.as_view(), name='bid'),