from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('profile/', views.profile, name='profile'),   # 🔥 önemli: name="profile"
    path('explore/', views.explore_profiles, name='explore_profiles'),  # diğer profilleri keşfet
    path('profile/<str:username>/', views.user_profile, name='user_profile'),  # detaylı profil
]
