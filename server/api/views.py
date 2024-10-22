from django.shortcuts import render
from rest_framework import viewsets

from .models import Board, Project, Task
from .serializers import BoardSerializer, ProjectSerializer, TaskSerializer

# Create your views here.


def index(request):
    return render(request, "index.html")


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class BoardViewSet(viewsets.ModelViewSet):
    serializer_class = BoardSerializer

    def get_queryset(self):
        return Board.objects.filter(project=self.kwargs["project_id"])


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    def get_queryset(self):
        return Task.objects.filter(board=self.kwargs["board_id"])