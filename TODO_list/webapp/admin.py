from django.contrib import admin
from webapp.models import Task, Status, Type


admin.site.register(Task)
admin.site.register(Type)
admin.site.register(Status)
