from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auctions/', include('auctions.urls')),
    path('users/', include('users.urls')),
    path('messages/', include('user_messages.urls')),
    path('rating/', include('rating.urls')),
    path('analytics/', include('analytics.urls')),
    path('reports/', include('reports.urls')),
]
