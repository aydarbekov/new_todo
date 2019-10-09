from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


from webapp.models import Project
from webapp.forms import TaskForm, ProjectForm
from webapp.views.base_views import MassDeleteView


class ProjectsListView(ListView):
    template_name = 'project/list.html'
    context_object_name = 'projects'
    model = Project
    ordering = 'created_at'
    paginate_by = 10
    paginate_orphans = 1


class ProjectsDelete(MassDeleteView):
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
class ProjectCreateView(CreateView):
    template_name = 'project/create.html'
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})


class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'project/update.html'
    form_class = ProjectForm
    context_object_name = 'obj'
    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})


class ProjectDeleteView(DeleteView):
    template_name = 'project/delete.html'
    model = Project
    context_object_name = 'obj'
    success_url = reverse_lazy('projects_view')

