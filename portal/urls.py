from django.urls import path

from portal.views import home

urlpatterns = [
    path('', home),
    
]
