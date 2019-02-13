from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from users import views

urlpatterns = [
    path('api-token-auth/', obtain_jwt_token, name='token-auth'),
    path('api-token-refresh/', refresh_jwt_token),
    path('api-token-verify/', verify_jwt_token, name='verify-token'),

    path('users/', views.UsersListCreateView.as_view(), name='users'),
]
