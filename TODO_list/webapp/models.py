from django.db import models

from django.db import models
status_choices = [('new', 'Новая'),('in_progress', 'В процессе'),('done', 'Сделано')]


class Project(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Название')
    description = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return self.name

class Task(models.Model):
    description = models.CharField(max_length=200, null=False, blank=False, verbose_name='Описание')
    full_descr = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Подробное описание')
    project = models.ForeignKey('Project', related_name='tasks', null=True, blank=False, on_delete=models.PROTECT, verbose_name='Проект')
    status = models.ForeignKey('Status', related_name='task_status', on_delete=models.PROTECT, verbose_name='Статус')
    type = models.ForeignKey('Type', related_name='task_type', on_delete=models.PROTECT, verbose_name='Тип')
    date = models.DateField(auto_now_add=True, verbose_name='Дата выполнения')
    update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления',null=True, blank=False)

    def __str__(self):
        return self.description


class Type(models.Model):
    type = models.CharField(max_length=40, verbose_name='Тип')

    def __str__(self):
        return self.type

class Status(models.Model):
    status = models.CharField(max_length=40, verbose_name='Статус')

    def __str__(self):
        return self.status
