"""blog_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth_view


urlpatterns = [
	# for /admin/
    path('admin/', admin.site.urls),
    # for /blog/
    path('blog/', include('blog.urls')),
    # These are for reseting the password, I could have done this in the blog/urls.py but I didn't Obviously for a reason
    # the reason is that django has a lot of inbluit functionality so, I'm using mostly django inbuilt stuff for reseting
    # the password, so, Django by default searches for these urls in the main urls.py file, so If I included these in blog/urls.py
    # file, it would give me an error
    path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='blog/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='blog/password_reset.html'), name="password_reset"),
    # for /blog/password-reset/done/
    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(template_name='blog/password_reset_done.html'), name="password_reset_done"),
    path('password-reset/complete/', auth_view.PasswordResetCompleteView.as_view(template_name='blog/password_reset_complete.html'), name="password_reset_complete"),
]
