from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


from webapp.models import Project
from webapp.forms import TaskForm
from webapp.views.base_views import MassDeleteView


class ProjectsListView(ListView):
    template_name = 'project/list.html'
    context_object_name = 'projects'
    model = Project
    ordering = 'created_at'
    paginate_by = 10
    paginate_orphans = 1


# class TasksDelete(MassDeleteView):
#     model = Task
#     url = 'index'
#
#
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
# class TaskCreateView(CreateView):
#     template_name = 'task/create.html'
#     model = Task
#     form_class = TaskForm
#
#     def get_success_url(self):
#         return reverse('task_view', kwargs={'pk': self.object.pk})
#
#
# class TaskUpdateView(UpdateView):
#     model = Task
#     template_name = 'task/update.html'
#     form_class = TaskForm
#     context_object_name = 'obj'
#     def get_success_url(self):
#         return reverse('task_view', kwargs={'pk': self.object.pk})
#
#
# class TaskDeleteView(DeleteView):
#     template_name = 'task/delete.html'
#     model = Task
#     context_object_name = 'obj'
#     success_url = reverse_lazy('index')
#
