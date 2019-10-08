from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import TemplateView
from django.views.generic.base import View

#delete with checkers
class MassDeleteView(TemplateView):
    model = None
    url = None

    def post(self, request, *args, **kwargs):
        delete = request.POST.getlist('del')
        self.model.objects.filter(pk__in=delete).delete()
        return redirect(self.url)