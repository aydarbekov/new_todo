from django.contrib import admin
from django.urls import path
from webapp.views import IndexView, TaskView, TaskCreateView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('task/<int:pk>/', TaskView.as_view(), name='task_view'),
    path('task/add/', TaskCreateView.as_view(), name='task_create'),
    path('task/<int:pk>/edit/', TaskUpdateView.as_view(), name = 'task_update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name = 'task_delete'),
    path('types/', TypesView.as_view(), name = 'types_view')
]
