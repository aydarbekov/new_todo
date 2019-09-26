from django.contrib import admin
from django.urls import path
from webapp.views import IndexView, TaskView, TaskCreateView, TaskUpdateView, TaskDeleteView, TypeView, TypeCreateView, \
    TypeUpdateView, TypeDeleteView, StatusView, StatusCreateView, StatusUpdateView, StatusDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('task/<int:pk>/', TaskView.as_view(), name='task_view'),
    path('task/add/', TaskCreateView.as_view(), name='task_create'),
    path('task/<int:pk>/edit/', TaskUpdateView.as_view(), name = 'task_update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name = 'task_delete'),
    path('types/', TypeView.as_view(), name = 'types_view'),
    path('types/add/', TypeCreateView.as_view(), name='type_create'),
    path('types/<int:pk>/edit/', TypeUpdateView.as_view(), name = 'type_update'),
    path('types/<int:pk>/delete/', TypeDeleteView.as_view(), name = 'type_delete'),
    path('statuses/', StatusView.as_view(), name='status_view'),
    path('status/add/', StatusCreateView.as_view(), name='status_create'),
    path('status/<int:pk>/edit/', StatusUpdateView.as_view(), name = 'status_update'),
    path('status/<int:pk>/delete/', StatusDeleteView.as_view(), name='status_delete'),

]
