from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect


from webapp.models import Status
from webapp.forms import StatusForm
from webapp.views.base_views import BaseDeleteView


class StatusView(ListView):
    template_name = 'status/list.html'
    context_object_name = 'statuses'
    model = Status


class StatusDelete(DeleteView):
    model = Status
    url = 'status_view'


class StatusCreateView(CreateView):
    template_name = 'status/create.html'
    model = Status
    form_class = StatusForm

    def get_success_url(self):
        return reverse('status_view')


class StatusUpdateView(UpdateView):
    model = Status
    template_name = 'status/update.html'
    form_class = StatusForm
    context_object_name = 'obj'
    def get_success_url(self):
        return reverse('status_view')


class StatusDeleteView(DeleteView):
    template_name = 'status/delete.html'
    model = Status
    context_object_name = 'obj'
    success_url = reverse_lazy('status_view')
