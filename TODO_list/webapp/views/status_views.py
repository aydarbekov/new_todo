from django.urls import reverse
from django.views.generic import TemplateView, ListView, CreateView
from django.shortcuts import render, get_object_or_404, redirect


from webapp.models import Status
from webapp.forms import StatusForm
from webapp.views.base_views import DeleteView, UpdateView


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
# class StatusUpdateView(TemplateView):
#
#     def get(self, request, **kwargs):
#         status = get_object_or_404(Status, pk=kwargs['pk'])
#         form = StatusForm(data={'status': status.status})
#         return render(request, 'status/update.html', context={'form': form, 'status': status})
#
#     def post(self, request, **kwargs):
#         status = get_object_or_404(Status, pk=kwargs['pk'])
#         form = StatusForm(data=request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             status.status = data['status']
#             status.save()
#             return redirect('status_view')
#         else:
#             return render(request, 'status/update.html', context={'form': form})


class StatusDeleteView(TemplateView):
    def get(self, request, *args, **kwargs):
        status = get_object_or_404(Status, pk=kwargs['pk'])
        return render(request, 'status/delete.html', context={'status': status})

    def post(self, request, **kwargs):
        status = get_object_or_404(Status, pk=kwargs['pk'])

        status.delete()
        return redirect('status_view')
