from django.urls import path

from . import views

urlpatterns = [
    path('', views.RatingView.as_view(), name='rating'),
]
