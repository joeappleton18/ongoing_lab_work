from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import BoardViewSet, ProjectViewSet, TaskViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'projects/(?P<project_id>\d+)/boards',
                BoardViewSet, basename='board')
router.register(r'projects/(?P<project_id>\d+)/boards/(?P<board_id>\d+)/tasks',
                TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
]
