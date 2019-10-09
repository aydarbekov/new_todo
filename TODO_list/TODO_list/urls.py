from django.contrib import admin
from django.urls import path
from webapp.views import IndexView, TaskView, TaskCreateView, TaskUpdateView, TaskDeleteView, TypeView, TypeCreateView, \
    TypeUpdateView, TypeDeleteView, StatusView, StatusCreateView, StatusUpdateView, StatusDeleteView
from webapp.views.project_views import ProjectsListView, ProjectView, ProjectCreateView, ProjectUpdateView, \
    ProjectDeleteView, ProjectsDelete
from webapp.views.status_views import StatusDelete
from webapp.views.task_views import TasksDelete, TaskForProjectCreateView
from webapp.views.type_views import TypeDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('task/<int:pk>/', TaskView.as_view(), name='task_view'),
    path('task/add/', TaskCreateView.as_view(), name='task_create'),
    path('task/<int:pk>/edit/', TaskUpdateView.as_view(), name = 'task_update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name = 'task_delete'),
    path('massdelete/', TasksDelete.as_view(), name='mass_delete'),
    path('types/', TypeView.as_view(), name = 'types_view'),
    path('types/add/', TypeCreateView.as_view(), name='type_create'),
    path('types/<int:pk>/edit/', TypeUpdateView.as_view(), name = 'type_update'),
    path('types/<int:pk>/delete/', TypeDeleteView.as_view(), name = 'type_delete'),
    path('massdeletetypes/', TypeDelete.as_view(), name='mass_delete_types'),
    path('statuses/', StatusView.as_view(), name='status_view'),
    path('status/add/', StatusCreateView.as_view(), name='status_create'),
    path('status/<int:pk>/edit/', StatusUpdateView.as_view(), name = 'status_update'),
    path('status/<int:pk>/delete/', StatusDeleteView.as_view(), name='status_delete'),
    path('massdeletestatus/', StatusDelete.as_view(), name='mass_delete_status'),
    path('projects/', ProjectsListView.as_view(), name='projects_view'),
    path('project/<int:pk>/', ProjectView.as_view(), name='project_view'),
    path('project/<int:pk>/add-task/', TaskForProjectCreateView.as_view(), name='project_task_create'),
    path('project/add/', ProjectCreateView.as_view(), name='project_create'),
    path('project/<int:pk>/edit/', ProjectUpdateView.as_view(), name='project_update'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    path('massdeleteprojects/', ProjectsDelete.as_view(), name='mass_delete_projects'),

]
