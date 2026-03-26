from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from projects.api import ProjectViewSet

router = routers.DefaultRouter()
router.register('api/projects', ProjectViewSet, 'projects')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]