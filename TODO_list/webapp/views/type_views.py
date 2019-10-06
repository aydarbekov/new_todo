from django.urls import reverse
from django.views.generic import TemplateView, ListView, CreateView
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View

from webapp.models import Type
from webapp.forms import TypeForm
from webapp.views.base_views import DeleteView


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


class TypeUpdateView(TemplateView):

    def get(self, request, **kwargs):
        type = get_object_or_404(Type, pk=kwargs['pk'])
        form = TypeForm(data={'type': type.type})
        return render(request, 'type/update.html', context={'form': form, 'type': type})

    def post(self, request, **kwargs):
        type = get_object_or_404(Type, pk=kwargs['pk'])
        form = TypeForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            type.type = data['type']
            type.save()
            return redirect('types_view')
        else:
            return render(request, 'type/update.html', context={'form': form})


class TypeDeleteView(TemplateView):
    def get(self, request, *args, **kwargs):
        type = get_object_or_404(Type, pk=kwargs['pk'])
        return render(request, 'type/delete.html', context={'type': type})

    def post(self, request, **kwargs):
        type = get_object_or_404(Type, pk=kwargs['pk'])

        type.delete()
        return redirect('types_view')
