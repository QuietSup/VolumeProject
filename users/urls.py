from django.urls import path
from users import views


app_name = 'users'

urlpatterns = [
    path('signup', views.signup_view, name='signup'),
    path('login', views.login_view, name='login'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('logout', views.logout_view, name='logout'),
]
