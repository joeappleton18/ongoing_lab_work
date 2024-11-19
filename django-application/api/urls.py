from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import BoardListsView, BoardViewSet, ProjectViewSet, TaskViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'projects/(?P<project_id>\d+)/boards',
                BoardViewSet, basename='board')

urlpatterns = [
    path('', include(router.urls)),
    path('projects/<int:project_pk>/boards/<int:board_pk>/lists/', 
     BoardListsView.as_view(), 
     name='board-lists'),
]
