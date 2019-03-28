from django.urls import path

from . import views

app_name = 'user_messages'

urlpatterns = [
    path('', views.ChatListCreateView.as_view(), name='chat-list'),
    path('<int:chat_pk>/', views.MessagesListCreateView.as_view(), name='messages-list'),
]
