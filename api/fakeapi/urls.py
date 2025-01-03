from django.contrib import admin
from django.urls import path, include
from fakeapi.views import *

urlpatterns = [
    path('health/', HealthyView.as_view(), name='token_obtain_pair'),
]
