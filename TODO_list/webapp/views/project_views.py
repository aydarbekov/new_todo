from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from accounts.models import Team
from webapp.models import Project
from webapp.forms import TaskForm, ProjectForm, SimpleSearchForm
from webapp.views.base_views import MassDeleteView
from django.db.models import Q
from django.utils.http import urlencode

class ProjectsListView(ListView):
    template_name = 'project/list.html'
    context_object_name = 'projects'
    model = Project
    ordering = 'created_at'
    paginate_by = 10
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
            query = Q(name__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None


class ProjectsDelete(LoginRequiredMixin, MassDeleteView):
    model = Project
    url = 'projects_view'


class ProjectView(DetailView):
    template_name = 'project/project.html'
    pk_url_kwarg = 'pk'
    model = Project

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['form'] = ArticleCommentForm()
    #     comments = context['article'].comments.order_by('-created_at')
    #     self.paginate_comments_to_context(comments, context)
    #     return context
    #
    # def paginate_comments_to_context(self, comments, context):
    #     paginator = Paginator(comments, 3, 0)
    #     page_number = self.request.GET.get('page', 1)
    #     page = paginator.get_page(page_number)
    #     context['paginator'] = paginator
    #     context['page_obj'] = page
    #     context['comments'] = page.object_list
    #     context['is_paginated'] = page.has_other_pages()
#


class ProjectCreateView(LoginRequiredMixin, CreateView):
    template_name = 'project/create.html'
    model = Project
    form_class = ProjectForm

    def form_valid(self, form):
        myself = self.request.user
        self.object = form.save()
        date = datetime.now()
        pk = self.object.pk
        Team.objects.create(user=myself, projects=self.object, start_date=date)
        return redirect('webapp:project_view', pk)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        pk = self.kwargs.get('pk')
        kwargs['project_pk'] = pk
        kwargs['myself'] = self.request.user
        return kwargs

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    template_name = 'project/update.html'
    form_class = ProjectForm
    context_object_name = 'obj'
    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'project/delete.html'
    model = Project
    context_object_name = 'obj'
    success_url = reverse_lazy('webapp:projects_view')

