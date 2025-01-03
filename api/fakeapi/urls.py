from django.contrib import admin
from django.urls import path, include
from fakeapi.views import *

urlpatterns = [
    path('health/', HealthyView.as_view(), name='health'),
    path('user/', UserView.as_view(), name='user'),
    path('admin/', AdminView.as_view(), name='admin'),
]
