from rest_framework import generics
from .models import Publicacion, Comentario
from .serializers import PublicacionSerializer, ComentarioSerializer

class PublicacionListCreate(generics.ListCreateAPIView):
    queryset = Publicacion.objects.all()
    serializer_class = PublicacionSerializer

class PublicacionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publicacion.objects.all()
    serializer_class = PublicacionSerializer