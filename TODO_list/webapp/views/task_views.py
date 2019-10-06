from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View

from webapp.models import Task
from webapp.forms import TaskForm
from webapp.views.base_views import DeleteView, UpdateView


class IndexView(ListView):
    template_name = 'task/index.html'
    context_object_name = 'tasks'
    model = Task
    ordering = '-date'
    paginate_by = 5
    paginate_orphans = 1


class TasksDelete(DeleteView):
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
    form_class = TaskForm
    template_name = 'task/update.html'
    model = Task
    redirect_url = 'task_view'

    def get_redirect_url(self):
        return reverse('task_view', kwargs={'pk': self.object.pk})

# , kwargs={'pk': self.object.pk})
# , kwargs['pk']

class TaskDeleteView(TemplateView):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        return render(request, 'task/delete.html', context={'task': task})

    def post(self, request, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])

        task.delete()
        return redirect('index')
