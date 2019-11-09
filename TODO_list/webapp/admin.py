from django.contrib import admin

from accounts.models import Profile, Team
from webapp.models import Task, Status, Type, Project
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class ProfileInline(admin.StackedInline):
    model = Profile
    fields = ['avatar', 'about', 'github_profile']


class ProfileAdmin(UserAdmin):
    inlines = [ProfileInline]

admin.site.register(Task)
admin.site.register(Type)
admin.site.register(Status)
admin.site.register(Project)
admin.site.unregister(User)
admin.site.register(User, ProfileAdmin)
admin.site.register(Team)
