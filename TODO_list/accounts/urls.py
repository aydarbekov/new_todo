from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from accounts.views import register_view, user_activate, UserDetailView, UserChangeView, UserPasswordChangeView, \
    ProfilesListView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', register_view, name='create'),
    path('register/activate/', user_activate, name='user_activate'),
    path('profile/<pk>/', UserDetailView.as_view(), name='user_detail'),
    path('profile/<pk>/edit', UserChangeView.as_view(), name='user_update'),
    path('profile/<pk>/change_password/', UserPasswordChangeView.as_view(), name='user_change_password'),
    path('profiles/', ProfilesListView.as_view(), name='profiles_list'),

]

app_name = 'accounts'
