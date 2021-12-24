from django.urls import path

from . import views
from .views import RegisterUser, LoginUser, AddPost

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.load_profile, name='profile'),
    path('profile/add/', AddPost.as_view(), name='add'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', views.logout_user, name='logout'),
]
