from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from accounts.views import register_view, user_activate

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', register_view, name='create'),
    path('register/activate/', user_activate, name='user_activate')
]

app_name = 'accounts'
