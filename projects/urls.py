from django.urls import path, include
from rest_framework import routers
from projects.api import ProjectViewSet

router = routers.DefaultRouter()
router.register('api/projects', ProjectViewSet, 'projects')

urlpatterns = [
    path('', include(router.urls)),
]