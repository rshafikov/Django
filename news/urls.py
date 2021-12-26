from django.urls import path
from .views import index, registration, registration_complete, new_post, draw


urlpatterns = [
    path('', index),
    path('registration', registration),
    path('registration/', registration_complete),
    path('new_post', new_post),
    path('draw/', draw),
]

