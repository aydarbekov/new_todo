from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View

from webapp.models import Task, Type, Status
from webapp.forms import TaskForm

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context

class TaskView(TemplateView):
    template_name = 'task_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs['pk'])
        return context


class TaskCreateView(View):

    def get(self, request, **kwargs):
        form = TaskForm()
        return render(request, 'task_create.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            task = Task.objects.create(description=data['description'], full_descr=data['full_descr'],
                                          status=data['status'], type=data['type'])
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'task_create.html', context={'form': form})
    #
    # if request.method == 'GET':
    #     form = TaskForm()
    #     return render(request, 'task_create.html', context={'form': form})
    # elif request.method == 'POST':
    #     form = TaskForm(data=request.POST)
    #     if form.is_valid():
    #         data = form.cleaned_data
    #         task = Article.objects.create(description=data['description'], full_descr=data['full_descr'],
    #                                       status=data['status'], date=data['date'])
    #         return redirect('task_view', pk=task.pk)
    #     else:
    #         return render(request, 'task_create.html', context={'form': form})