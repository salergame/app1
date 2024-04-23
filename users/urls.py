from django.urls import path
from users import views

from django.contrib.auth.views import (
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

app_name='users'

urlpatterns = [
    path('login/',views.login ,name='login'),
    path('registration/',views.registration,name='registration'),
    path('profile/',views.profile,name='profile'),
    path('users-cart/',views.users_cart,name='users_cart'),
    path('logout/',views.logout,name='logout'),
    path('password-reset/', PasswordResetView.as_view(template_name='users/password_reset.html',html_email_template_name='users/password_reset_email.html'),name='password-reset'),
    path('user/password-reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete'),
]