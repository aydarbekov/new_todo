from django import forms
from django.forms import widgets

from webapp.models import Type, Status, Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['description', 'full_descr', 'status', 'type']


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['type']


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['status']