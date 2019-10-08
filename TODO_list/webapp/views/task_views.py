from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View

from webapp.models import Task
from webapp.forms import TaskForm
from webapp.views.base_views import MassDeleteView


class IndexView(ListView):
    template_name = 'task/index.html'
    context_object_name = 'tasks'
    model = Task
    ordering = '-date'
    paginate_by = 5
    paginate_orphans = 1


class TasksDelete(MassDeleteView):
    model = Task
    url = 'index'


class TaskView(DetailView):
    template_name = 'task/task.html'
    pk_url_kwarg = 'pk'
    model = Task


class TaskCreateView(CreateView):
    template_name = 'task/create.html'
    model = Task
    form_class = TaskForm

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.object.pk})


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'task/update.html'
    form_class = TaskForm
    context_object_name = 'obj'
    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.object.pk})


class TaskDeleteView(DeleteView):
    template_name = 'task/delete.html'
    model = Task
    context_object_name = 'obj'
    success_url = reverse_lazy('index')

