from django.urls import path

from users.views import user, login_view, refresh_token_view

urlpatterns = [
    path('user', user, name='user'),
    path('login', login_view, name='login'),
    path('refresh_token', refresh_token_view, name='refresh_token'),
]