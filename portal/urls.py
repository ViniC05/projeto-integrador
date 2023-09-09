from django.urls import path

from . import views

app_name = 'portal'

urlpatterns = [
    path('', views.home, name="home"),
    path('portal/search/', views.search, name="search"),
    path('portal/category/<int:category_id>/', views.category, name="category"),
    path('post/<int:id>/', views.post_portal, name="post"),
    path('portal/login/', views.login_view, name='login'),
    path('post/<int:post_id>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    
]
