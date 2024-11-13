from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response

from .models import Board, List, Project, Task
from .serializers import (BoardSerializer, ListSerializer, ProjectSerializer,
                          TaskSerializer)

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


class BoardListsView(generics.RetrieveAPIView):
    queryset = Board.objects.all()
    serializer_class = ListSerializer

    def get(self, request, *args, **kwargs):
        board = self.get_object()
        lists = List.objects.filter(board=board)
        print(lists)
        serializer = ListSerializer(lists, many=True)
        return Response(serializer.data)
