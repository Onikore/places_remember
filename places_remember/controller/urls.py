from django.urls import path

from . import views
from .views import RegisterUser, LoginUser, AddPost

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.load_profile, name='profile'),
    path('profile/delete/<slug:post_slug>/', views.delete_post, name='delete_post'),
    path('profile/add/', AddPost.as_view(), name='add'),
    path('profile/<slug:post_slug>/', views.view_post, name='view_post'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', views.logout_user, name='logout'),
]
