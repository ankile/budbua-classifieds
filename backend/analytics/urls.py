from django.urls import path

from analytics import views

urlpatterns = [
    path('/', views.OwnerAnalyticsView.as_view(), name='owner-analytics'),

]
