from django.urls import path

from . import views

app_name = 'authors'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('register/create/', views.register_create, name='register_create'),
    path('login/', views.login_view, name='login'),
    path('login/create/', views.login_create, name='login_create'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/post/novo/', views.dashboard_portal_novo, name='dashboard_portal_novo'),
    path('dashboard/post/<int:id>/edit/', views.dashboard_portal_edit, name='dashboard_portal_edit'),
    path('dashboard/post/<int:id>/delete/', views.dashboard_portal_delete, name='dashboard_portal_delete'),
    
]
