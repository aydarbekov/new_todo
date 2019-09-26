from django.contrib import admin
from django.urls import path
from webapp.views import IndexView, TaskView, TaskCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('task/<int:pk>/', TaskView.as_view(), name='task_view'),
    path('task/add/', TaskCreateView.as_view(), name='task_create')
]
