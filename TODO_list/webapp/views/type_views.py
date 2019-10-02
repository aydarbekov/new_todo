from django.views.generic import TemplateView, ListView
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View

from webapp.models import Type
from webapp.forms import TypeForm


class TypeView(ListView):
    context_object_name = 'types'
    model = Type
    template_name = 'type/list.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['types'] = Type.objects.all()
    #     return context
    #
    # def post(self, request, *args, **kwargs):
    #     type_del = request.POST.getlist('del')
    #     Type.objects.filter(pk__in=type_del).delete()
    #     return redirect('types_view')


class TypeCreateView(View):

    def get(self, request, **kwargs):
        form = TypeForm()
        return render(request, 'type/create.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = TypeForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Type.objects.create(type=data['type'])
            return redirect('types_view')
        else:
            return render(request, 'type/create.html', context={'form': form})


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
