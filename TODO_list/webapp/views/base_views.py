from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView

class DeleteView(TemplateView):
    model = None
    url = None

    def post(self, request, *args, **kwargs):
        delete = request.POST.getlist('del')
        self.model.objects.filter(pk__in=delete).delete()
        return redirect(self.url)