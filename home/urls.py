from .views import home_View
from django.urls import path

urlpatterns = [
    path('', home_View, name='home'),
    
]