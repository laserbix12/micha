from rest_framework import serializers
from .models import Project
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'Descripcion', 'Tecnologias', 'f_creacion')
        read_only_fields = ('f_creacion',)