from rest_framework.serializers import ModelSerializer
from comentarios.models import Comentario

class ComentarioSerializer(ModelSerializer):
    class Meta:
        model = Comentario
        fiels = ['id', 'usuario', 'comentario', 'data', 'aprovado']

