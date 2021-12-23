from django.urls import path
from .views import index, registration, reg_2


urlpatterns = [
    path('', index),
    path('registration', registration),
    path('registration/', reg_2),
]