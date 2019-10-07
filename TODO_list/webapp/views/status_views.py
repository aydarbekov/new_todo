from django.urls import reverse
from django.views.generic import TemplateView, ListView, CreateView
from django.shortcuts import render, get_object_or_404, redirect


from webapp.models import Status
from webapp.forms import StatusForm
from webapp.views.base_views import DeleteView, UpdateView, BaseDeleteView


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
    form_class = StatusForm
    template_name = 'status/update.html'
    model = Status
    redirect_url = 'status_view'

class StatusDeleteView(BaseDeleteView):
    model = Status
    template_name = 'status/delete.html'
    redirect_url = 'status_view'
    podtv = False
