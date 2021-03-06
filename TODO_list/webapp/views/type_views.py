from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View

from webapp.models import Type
from webapp.forms import TypeForm
from webapp.views.base_views import MassDeleteView


class TypeView(ListView):
    context_object_name = 'types'
    model = Type
    template_name = 'type/list.html'


class TypeDelete(LoginRequiredMixin, MassDeleteView):
    model = Type
    url = 'types_view'


class TypeCreateView(LoginRequiredMixin, CreateView):
    template_name = 'type/create.html'
    model = Type
    form_class = TypeForm

    def get_success_url(self):
        return reverse('webapp:types_view')


class TypeUpdateView(LoginRequiredMixin, UpdateView):
    model = Type
    template_name = 'type/update.html'
    form_class = TypeForm
    context_object_name = 'obj'
    def get_success_url(self):
        return reverse('webapp:types_view')


class TypeDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'type/delete.html'
    model = Type
    context_object_name = 'obj'
    success_url = reverse_lazy('webapp:types_view')

