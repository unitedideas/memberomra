from django.urls import path

from members.forms import CustomAuthForm
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('search', views.search, name='search'),

    path('add', views.add, name='add'),

    path('', auth_views.LoginView.as_view(template_name='members/home.html', authentication_form=CustomAuthForm,
                                          redirect_authenticated_user=True), name='login'),

    path('logout/', auth_views.LogoutView.as_view(template_name='members/logout.html'), name='logout'),

    path('password_reset', auth_views.PasswordResetView.as_view(template_name='members/password_reset.html'),
         name='password_reset'),

    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='members/password_reset_done.html'),
         name='password_reset_done'),

    path('password-reset/confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='members/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('password-reset/complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='members/password_reset_complete.html'),
         name='password_reset_complete'),

    path('profile/password/', auth_views.PasswordChangeView.as_view(template_name='members/password_change.html'),
         name='password_change'),

    path('profile/password/done',
         auth_views.PasswordChangeDoneView.as_view(template_name='members/password_change_done.html'),
         name='password_change_done'),

]
