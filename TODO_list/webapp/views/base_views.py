from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView


class DetailView(TemplateView):
    context_key = 'objects'
    model = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[self.context_key] = get_object_or_404(self.model, pk=kwargs['pk'])
        return context

class DeleteView(TemplateView):
    model = None
    url = None

    def post(self, request, *args, **kwargs):
        delete = request.POST.getlist('del')
        self.model.objects.filter(pk__in=delete).delete()
        return redirect(self.url)