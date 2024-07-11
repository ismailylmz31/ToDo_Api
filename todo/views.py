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




# # Create
# class ToDoCreate(APIView):
#     def post(self, request, format=None):
#         serializer = ToDoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # Read (List)
# class ToDoList(APIView):
#     def get(self, request, format=None):
#         todos = ToDo.objects.all()
#         serializer = ToDoSerializer(todos, many=True)
#         return Response(serializer.data)

# # Read (Detail)
# class ToDoDetail(APIView):
#     def get(self, request, pk, format=None):
#         try:
#             todo = ToDo.objects.get(pk=pk)
#         except ToDo.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
        
#         serializer = ToDoSerializer(todo)
#         return Response(serializer.data)

# # Update
# class ToDoUpdate(APIView):
#     def put(self, request, pk, format=None):
#         try:
#             todo = ToDo.objects.get(pk=pk)
#         except ToDo.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#         serializer = ToDoSerializer(todo, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # Delete
# class ToDoDelete(APIView):
#     def delete(self, request, pk, format=None):
#         try:
#             todo = ToDo.objects.get(pk=pk)
#         except ToDo.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
        
#         todo.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)