from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View

from webapp.models import Task, Project
from webapp.forms import TaskForm, ProjectTaskForm, SimpleSearchForm
from webapp.views.base_views import MassDeleteView
from django.db.models import Q
from django.utils.http import urlencode


class IndexView(ListView):
    template_name = 'task/index.html'
    context_object_name = 'tasks'
    model = Task
    ordering = '-date'
    paginate_by = 5
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(description__icontains=self.search_value) | Q(full_descr__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None


class TasksDelete(UserPassesTestMixin, MassDeleteView):
    model = Task
    url = 'index'

    def test_func(self):
        project = self.get_project()
        print(self.request.user)
        users = User.objects.filter(team_user__projects=project)
        if self.request.user in users:
            return True
        return False

    def get_project(self):
        return get_object_or_404(Project, pk=self.kwargs.get('pk'))


class TaskView(DetailView):
    template_name = 'task/task.html'
    pk_url_kwarg = 'pk'
    model = Task

#
# class TaskCreateView(LoginRequiredMixin, CreateView):
#     template_name = 'task/create.html'
#     model = Task
#     form_class = TaskForm
#
#     def get_success_url(self):
#         return reverse('task_view', kwargs={'pk': self.object.pk})


class TaskUpdateView(UserPassesTestMixin, UpdateView):
    model = Task
    template_name = 'task/update.html'
    form_class = TaskForm
    context_object_name = 'obj'

    def test_func(self):
        project = self.get_project()
        print(self.request.user)
        users = User.objects.filter(team_user__projects=project)
        if self.request.user in users:
            return True
        return False

    def get_project(self):
        return get_object_or_404(Project, pk=self.kwargs.get('pk'))

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.object.pk})


class TaskDeleteView(UserPassesTestMixin, DeleteView):
    template_name = 'task/delete.html'
    model = Task
    context_object_name = 'obj'
    success_url = reverse_lazy('webapp:index')

    def test_func(self):
        project = self.get_project()
        print(self.request.user)
        users = User.objects.filter(team_user__projects=project)
        if self.request.user in users:
            return True
        return False

    def get_project(self):
        return get_object_or_404(Project, pk=self.kwargs.get('pk'))


class TaskForProjectCreateView(UserPassesTestMixin, CreateView):
    template_name = 'task/create.html'
    form_class = ProjectTaskForm

    def test_func(self):
        project = self.get_project()
        print(self.request.user)
        users = User.objects.filter(team_user__projects=project)
        if self.request.user in users:
            return True
        return False

    def get_project(self):
        return get_object_or_404(Project, pk=self.kwargs.get('pk'))

    def form_valid(self, form):
        project_pk = self.kwargs.get('pk')
        project = get_object_or_404(Project, pk=project_pk)
        project.tasks.create(**form.cleaned_data)
        return redirect('webapp:project_view', pk=project_pk)