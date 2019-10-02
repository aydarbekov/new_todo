from django.views.generic import TemplateView, ListView
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View

from webapp.models import Status
from webapp.forms import StatusForm


class StatusView(ListView):
    template_name = 'status/list.html'
    context_object_name = 'statuses'
    model = Status

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['statuses'] = Status.objects.all()
    #     return context
    #
    # def post(self, request, *args, **kwargs):
    #     status_del = request.POST.getlist('del')
    #     Status.objects.filter(pk__in=status_del).delete()
    #     return redirect('status_view')


class StatusCreateView(View):

    def get(self, request, **kwargs):
        form = StatusForm()
        return render(request, 'status/create.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = StatusForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Status.objects.create(status=data['status'])
            return redirect('status_view')
        else:
            return render(request, 'status/create.html', context={'form': form})

class StatusUpdateView(TemplateView):

    def get(self, request, **kwargs):
        status = get_object_or_404(Status, pk=kwargs['pk'])
        form = StatusForm(data={'status': status.status})
        return render(request, 'status/update.html', context={'form': form, 'status': status})

    def post(self, request, **kwargs):
        status = get_object_or_404(Status, pk=kwargs['pk'])
        form = StatusForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            status.status = data['status']
            status.save()
            return redirect('status_view')
        else:
            return render(request, 'status/update.html', context={'form': form})


class StatusDeleteView(TemplateView):
    def get(self, request, *args, **kwargs):
        status = get_object_or_404(Status, pk=kwargs['pk'])
        return render(request, 'status/delete.html', context={'status': status})

    def post(self, request, **kwargs):
        status = get_object_or_404(Status, pk=kwargs['pk'])

        status.delete()
        return redirect('status_view')