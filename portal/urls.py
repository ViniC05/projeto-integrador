from django.urls import path

from . import views

app_name = 'portal'

urlpatterns = [
    path('', views.home, name="home"),
    path('portal/search/', views.search, name="search"),
    path('portal/category/<int:category_id>/', views.category, name="category"),
    path('contato/<int:id>/', views.post_portal, name="post"),
    
]
