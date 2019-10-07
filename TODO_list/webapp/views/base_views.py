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
    podtv = None
    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(self.model, pk=kwargs['pk'])
        return render(request, self.template_name, context={'obj': obj})

    def post(self, request, **kwargs):
        obj = get_object_or_404(self.model, pk=kwargs['pk'])
        obj.delete()
        return redirect(self.redirect_url)

class UpdateView(View):
    form_class = None
    template_name = None
    model = None
    redirect_url = ''
    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(self.model, pk=kwargs['pk'])
        form = self.form_class(instance=obj)
        context = {'form': form, 'obj': obj}
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(self.model, pk=kwargs['pk'])
        form = self.form_class(instance=obj, data=request.POST)
        self.object = form.save()
        return redirect(self.get_redirect_url())

    def get_redirect_url(self):
        return self.redirect_url
