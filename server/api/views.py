from rest_framework import viewsets
from .models import Project
from .serializers import ProjectSerializer
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer