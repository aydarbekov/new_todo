from django import forms
from django.contrib.auth.models import User
from django.forms import widgets

from webapp.models import Type, Status, Task, Project


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['description', 'full_descr', 'project', 'status', 'type']


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['type']


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['status']


class ProjectTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['description', 'full_descr', 'status', 'type']


class ProjectForm(forms.ModelForm):
    users = forms.ModelMultipleChoiceField(queryset=User.objects.all(), required=False)

    def __init__(self, project_pk, myself, **kwargs):
        super().__init__(**kwargs)
        print(project_pk, 'PROJECTPK')
        # self.fields['user'].queryset = Team.objects.filter(project__id=project_pk)
        self.fields['users'].queryset = User.objects.exclude(username=myself)

    class Meta:
        model = Project
        fields = ['name', 'description', 'users']


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")