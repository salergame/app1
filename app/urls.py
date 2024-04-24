"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib.auth.views import (
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from app import settings

urlpatterns = [
    path('password-reset/', PasswordResetView.as_view(template_name='users/password_reset.html'),name='password-reset'),
    path('user/password-reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('user/password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),
    path('user/password-reset-complete/',PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete'),
    path('admin/', admin.site.urls),
    path('',include('main.urls', namespace='main')),
    path('catalog/',include('goods.urls', namespace='catalog')),
    path('user/',include('users.urls', namespace='user')),
    path('cart/',include('carts.urls', namespace='cart')),
    path('orders/', include('orders.urls',namespace='orders')),
    path("api/", include("api.urls")),
    path('delivery/',include('delivery.urls',namespace='delivery')),
    path('accounts/', include('allauth.urls')),

]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
        
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)