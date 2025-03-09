from django.urls import path
from .views import raspberry

urlpatterns = [
    path('', raspberry, name='raspberry'),
]
