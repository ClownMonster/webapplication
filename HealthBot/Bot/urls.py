from django.urls import path
from .views import landingScreen

urlpatterns = [

    path('',landingScreen,name='landingscreen'),
]
