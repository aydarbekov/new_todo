from django.urls import reverse
from django.views.generic import TemplateView, ListView, CreateView
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View

from webapp.models import Type
from webapp.forms import TypeForm
from webapp.views.base_views import DeleteView, UpdateView, BaseDeleteView


class TypeView(ListView):
    context_object_name = 'types'
    model = Type
    template_name = 'type/list.html'


class TypeDelete(DeleteView):
    model = Type
    url = 'types_view'


class TypeCreateView(CreateView):
    template_name = 'type/create.html'
    model = Type
    form_class = TypeForm

    def get_success_url(self):
        return reverse('types_view')

class TypeUpdateView(UpdateView):
    form_class = TypeForm
    template_name = 'type/update.html'
    model = Type
    redirect_url = 'types_view'

class TypeDeleteView(BaseDeleteView):
    model = Type
    template_name = 'type/delete.html'
    redirect_url = 'types_view'

