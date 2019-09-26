from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View

from webapp.models import Task, Type, Status
from webapp.forms import TaskForm, TypeForm, StatusForm


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


class TaskUpdateView(TemplateView):

    def get(self, request, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        form = TaskForm(data={'description': task.description, 'full_descr': task.full_descr, 'status': task.status,
                              'type': task.type})
        return render(request, 'update.html', context={'form': form, 'task': task})

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
            return render(request, 'update.html', context={'form': form})


class TaskDeleteView(TemplateView):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        return render(request, 'delete.html', context={'task': task})

    def post(self, request, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])

        task.delete()
        return redirect('index')


class TypeView(TemplateView):

    template_name = 'types.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['types'] = Type.objects.all()
        return context


class TypeCreateView(View):

    def get(self, request, **kwargs):
        form = TypeForm()
        return render(request, 'type_create.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = TypeForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Type.objects.create(type=data['type'])
            return redirect('types_view')
        else:
            return render(request, 'type_create.html', context={'form': form})


class TypeUpdateView(TemplateView):

    def get(self, request, **kwargs):
        type = get_object_or_404(Type, pk=kwargs['pk'])
        form = TypeForm(data={'type': type.type})
        return render(request, 'type_update.html', context={'form': form, 'type': type})

    def post(self, request, **kwargs):
        type = get_object_or_404(Type, pk=kwargs['pk'])
        form = TypeForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            type.type = data['type']
            type.save()
            return redirect('types_view')
        else:
            return render(request, 'type_update.html', context={'form': form})


class TypeDeleteView(TemplateView):
    def get(self, request, *args, **kwargs):
        type = get_object_or_404(Type, pk=kwargs['pk'])
        return render(request, 'type_delete.html', context={'type': type})

    def post(self, request, **kwargs):
        type = get_object_or_404(Type, pk=kwargs['pk'])

        type.delete()
        return redirect('types_view')


class StatusView(TemplateView):

    template_name = 'status_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['statuses'] = Status.objects.all()
        return context


class StatusCreateView(View):

    def get(self, request, **kwargs):
        form = StatusForm()
        return render(request, 'status_create.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = StatusForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Status.objects.create(status=data['status'])
            return redirect('status_view')
        else:
            return render(request, 'status_create.html', context={'form': form})

class StatusUpdateView(TemplateView):

    def get(self, request, **kwargs):
        status = get_object_or_404(Status, pk=kwargs['pk'])
        form = StatusForm(data={'status': status.status})
        return render(request, 'status_update.html', context={'form': form, 'status': status})

    def post(self, request, **kwargs):
        status = get_object_or_404(Status, pk=kwargs['pk'])
        form = StatusForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            status.status = data['status']
            status.save()
            return redirect('status_view')
        else:
            return render(request, 'status_update.html', context={'form': form})


class StatusDeleteView(TemplateView):
    def get(self, request, *args, **kwargs):
        status = get_object_or_404(Status, pk=kwargs['pk'])
        return render(request, 'status_delete.html', context={'status': status})

    def post(self, request, **kwargs):
        status = get_object_or_404(Status, pk=kwargs['pk'])

        status.delete()
        return redirect('status_view')