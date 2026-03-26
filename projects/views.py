from rest_framework import viewsets
from .models import Project
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
# Este archivo puede quedar vacío o eliminarse si usas api.py
# para definir tus ViewSets.
pass