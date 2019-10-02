from django.views.generic import TemplateView, ListView
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View

from webapp.models import Task
from webapp.forms import TaskForm
from webapp.views.base_views import DetailView, DeleteView


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

    # Добавить удаление галочками
    # def post(self, request, *args, **kwargs):
    #     task_del = request.POST.getlist('del')
    #     Task.objects.filter(pk__in=task_del).delete()
    #     return redirect('index')

class TaskView(DetailView):
    template_name = 'task/task.html'
    context_key = 'task'
    model = Task

class TaskCreateView(View):

    def get(self, request, **kwargs):
        form = TaskForm()
        return render(request, 'task/create.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            task = Task.objects.create(description=data['description'], full_descr=data['full_descr'],
                                          status=data['status'], type=data['type'])
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'task/create.html', context={'form': form})


class TaskUpdateView(TemplateView):

    def get(self, request, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        form = TaskForm(data={'description': task.description, 'full_descr': task.full_descr, 'status': task.status,
                              'type': task.type})
        return render(request, 'task/update.html', context={'form': form, 'task': task})

    def post(self, request, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        form = TaskForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            task.description = data['description']
            task.full_descr = data['full_descr']
            task.status = data['status']
            task.type = data['type']
            task.save()
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'task/update.html', context={'form': form})


class TaskDeleteView(TemplateView):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        return render(request, 'task/delete.html', context={'task': task})

    def post(self, request, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])

        task.delete()
        return redirect('index')
