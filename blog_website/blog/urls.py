from django.conf.urls import url
from django.contrib.auth import views as auth_view
# from users import views as user_views
from .views import index, content, register, profile, home, create_post, update_post, delete_post, User_Post_Profile
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

app_name = "blog"

urlpatterns = [
	# for /blog/
    # path('', index, name="index"),
    # fo /blog/
    path('', home.as_view(), name="index"),
    # for /blog/<username>
    path('user/<str:username>/', User_Post_Profile.as_view(), name="post-profile"),
    # for /blog/post/new/
    path('post/new/', create_post.as_view(), name="create-post"),
    # for /blog/post/pk/update
    path('post/<int:pk>/update/', update_post.as_view(), name="update-post"),
    # for /blog/post/pk/delete
    path('post/<int:pk>/delete/', delete_post.as_view(), name="delete-post"),
	# for /blog/343/, where 343 can be any number
    path('post/<int:pk>/', content, name="post-content"),
    # for /blog/register/
    path('register/', register, name="register"),
    # for /blog/login/
    path('login/', auth_view.LoginView.as_view(template_name='blog/login.html'), name="login"),
    # for /blog/password-reset/
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='blog/password_reset.html'), name="password_reset"),
    # for /blog/password-reset/done/
    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(template_name='blog/password_reset_done.html'), name="password_reset_done"),
    # For /blog/password-reset-confirm/<uidb64>/<token>/
    path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='blog/password_reset_confirm.html'), name='password_reset_confirm'),
    # for /blog/logout/
    path('logout/', auth_view.LogoutView.as_view(template_name='blog/logout.html'), name="logout"),
    # for /blog/profile/
    path('profile/', profile, name="profile"),

] 
#Above line is for the media_root and media_url we did in the settings of the website, it's kinda tough to
# understand, so just replace this or hop over to the documentation


if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

