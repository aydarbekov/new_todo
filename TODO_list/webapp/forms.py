from django import forms
from django.forms import widgets

from webapp.models import Type, Status


class TaskForm(forms.Form):
    description = forms.CharField(max_length=200, required=True, label='Описание')
    full_descr = forms.CharField(max_length=3000, required=False, label='Подробное описание')
    status = forms.ModelChoiceField(queryset=Status.objects.all(), required=True, widget=forms.Select)
    type = forms.ModelChoiceField(queryset=Type.objects.all(), required=True, widget=forms.Select)


class TypeForm(forms.Form):
    type = forms.CharField(max_length=40, required=True, label='Тип')


class StatusForm(forms.Form):
    status = forms.CharField(max_length=40, required=True, label='Статус')