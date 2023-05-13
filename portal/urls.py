from django.urls import path

from portal.views import home, sobre

urlpatterns = [
    path('', home),
    path('sobre/', sobre),
]