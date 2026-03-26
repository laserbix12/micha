from django.urls import path, include
from rest_framework import routers
from projects.views import ProjectViewSet

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]