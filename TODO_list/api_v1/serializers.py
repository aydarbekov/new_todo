from webapp.models import Task, Project, Type, Status

from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'description', 'full_descr', 'project', 'status', 'type', 'date', 'update')


class ProjectSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)
    class Meta:
        model = Project
        fields = ('id', 'name', 'created_at', 'updated_at', 'tasks')


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('id', 'type')


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('id', 'status')