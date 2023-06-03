from rest_framework import serializers
from .models import Sprint, Ticket
from core.models import project, milestone, User

class sprintSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)
    start_date = serializers.DateField(required=True)
    end_date = serializers.DateField(required=True)
    project = serializers.PrimaryKeyRelatedField(queryset=project.objects.all())
    milestone = serializers.PrimaryKeyRelatedField(queryset=milestone.objects.all())
    

    class Meta:
        model = Sprint
        fields = ['id', 'project', 'milestone', 'title', 'start_date', 'end_date']

class ticketSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)
    start_date = serializers.DateField(required=True)
    end_date = serializers.DateField(required=True)
    creator = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    assignee = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    sprint = serializers.PrimaryKeyRelatedField(queryset=Sprint.objects.all())    
    status = serializers.CharField()
    creator_name = serializers.PrimaryKeyRelatedField(read_only = True, source='creator.name')
    assignee_name = serializers.PrimaryKeyRelatedField(read_only = True, source='assignee.name')

    class Meta:
        model = Ticket
        # fields = "__all__"
        fields = ['id', 'sprint', 'title', 'description', 'start_date', 'end_date', 'assignee', 'creator', 'assignee_name', 'creator_name', 'status']