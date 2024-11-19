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
        project_pk = self.kwargs.get('project_pk')
        board_pk = self.kwargs.get('board_pk')

        # Retrieve the board and optionally validate project association
        try:
            board = Board.objects.get(pk=board_pk, project_id=project_pk)
        except Board.DoesNotExist:
            return Response(
                {"detail": "Board not found for this project."},
                status=status.HTTP_404_NOT_FOUND
            )

        # Retrieve lists associated with the board
        lists = List.objects.filter(board=board)
        serializer = ListSerializer(lists, many=True)
        return Response(serializer.data)