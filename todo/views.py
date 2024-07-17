from rest_framework import viewsets, status,generics, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ToDo, Photo
from .serializers import ToDoSerializer,PhotoSerializer
from rest_framework.views import APIView
import django_filters.rest_framework


class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    

# Create
class ToDoCreate(generics.CreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

# Read (List)
class ToDoList(generics.ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['completed']  # completed durumuna göre filtreleme
    search_fields = ['title']  # title'a göre arama

# Read (Detail)
class ToDoDetail(generics.RetrieveAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

# Update
class ToDoUpdate(generics.UpdateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

# Delete
class ToDoDelete(generics.DestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer




