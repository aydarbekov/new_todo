from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import TemplateView
from django.views.generic.base import View


class DeleteView(TemplateView):
    model = None
    url = None

    def post(self, request, *args, **kwargs):
        delete = request.POST.getlist('del')
        self.model.objects.filter(pk__in=delete).delete()
        return redirect(self.url)


class BaseDeleteView(TemplateView):
    model = None
    template_name = None
    redirect_url = ''
    podtv = True
    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(self.model, pk=kwargs['pk'])
        if self.podtv == True:
            return render(request, self.template_name, context={'obj': obj})
        elif self.podtv == False:
            obj.delete()
            return redirect(self.redirect_url)

    def post(self, request, **kwargs):
        obj = get_object_or_404(self.model, pk=kwargs['pk'])
        obj.delete()
        return redirect(self.redirect_url)