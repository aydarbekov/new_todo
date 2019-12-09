from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from api_v1 import views

router = routers.DefaultRouter()
router.register(r'tasks', views.TaskViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'types', views.TypeViewSet)
router.register(r'statuses', views.StatusViewSet)

app_name = 'api_v1'

urlpatterns = [
    path('', include(router.urls)),
    path('login/', obtain_auth_token, name='api_token_auth')
]