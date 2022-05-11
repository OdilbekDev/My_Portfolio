from django.urls import path
from .views import *

urlpatterns = [
    path('', Index, name="Index")
]