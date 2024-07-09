from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ToDo, Photo
from .serializers import ToDoSerializer,PhotoSerializer, BatchDeleteSerializer

class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


@api_view(['DELETE'])
def delete_multiple_todos(request):
    serializer = BatchDeleteSerializer(data=request.data)
    if serializer.is_valid():
        ids = serializer.validated_data['ids']
        todos = ToDo.objects.filter(id__in=ids)
        count, _ = todos.delete()
        return Response({"message": f"{count} To-Do items were deleted."}, status=status.HTTP_204_NO_CONTENT)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)