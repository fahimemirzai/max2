from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView,PasswordResetView,PasswordResetDoneView



app_name='account'
urlpatterns = [

    path('login/',LoginView.as_view(template_name='account/login.html'),name='login'),
    path('logout/', LogoutView.as_view(template_name='account/logout.html'), name='logout'),
    path('register/',views.register,name='register'),
    path('profile/',views.profile,name='profile'),
    path('profile/edit/',views.edit_profile,name='edit_profile'),
    path('password_change/', views.password_change, name='password_change'),
    path('password_reset/',PasswordResetView.as_view(template_name='account/password_reset.html'),name='password_reset'),
   #path('password_reset/done', PasswordResetDoneView.as_view(), name='password_reset_done'),





]