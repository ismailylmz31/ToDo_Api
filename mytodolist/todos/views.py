from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import Todo, CustomUser
from .serializers import TodoSerializer, UserSerializer
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.contrib.auth import get_user_model
import jwt

@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        username = data['username']
        password = data['password']
        user = CustomUser.objects.create_user(username=username, password=password)
        return JsonResponse(UserSerializer(user).data)

@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        username = data['username']
        password = data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return JsonResponse({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return JsonResponse({'error': 'Giriş kabul edilmedi'}, status=400)



def get_user_from_token(request):
    auth_header = request.headers.get('Authorization')
    if auth_header is not None and auth_header.startswith('Bearer '):
        token = auth_header.split(' ')[1]
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user_id = payload.get('user_id')
            user = get_user_model().objects.get(id=user_id)
            return user
        except (jwt.ExpiredSignatureError, jwt.DecodeError, get_user_model().DoesNotExist):
            return None
    return None



@csrf_exempt
def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'message': 'Logout başarılı'})

@csrf_exempt
def todo_list(request):
    user = get_user_from_token(request)
    if user is not None:
        if request.method == 'GET':
            todos = Todo.objects.filter(user=user)
            serializer = TodoSerializer(todos, many=True)
            return JsonResponse(serializer.data, safe=False)
    return JsonResponse({'error': 'Giriş yapılmadı'}, status=401)

@csrf_exempt
def todo_detail(request, pk):
    user = get_user_from_token(request)
    if user is not None:
        try:
            todo = Todo.objects.get(pk=pk, user=user)
        except Todo.DoesNotExist:
            return JsonResponse({'error': 'Todo bulunamadı'}, status=404)

        if request.method == 'GET':
            serializer = TodoSerializer(todo)
            return JsonResponse(serializer.data)
    return JsonResponse({'error': 'Giriş yapılmadı'}, status=401)

@csrf_exempt
def todo_update(request, pk):
    user = get_user_from_token(request)
    if user is not None:
        try:
            todo = Todo.objects.get(pk=pk, user=user)
        except Todo.DoesNotExist:
            return JsonResponse({'error': 'Todo bulunamadı'}, status=404)

        if request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = TodoSerializer(todo, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return JsonResponse(serializer.errors, status=400)
    return JsonResponse({'error': 'Giriş yapılmadı'}, status=401)

@csrf_exempt
def todo_delete(request, pk):
    user = get_user_from_token(request)
    if user is not None:
        try:
            todo = Todo.objects.get(pk=pk, user=user)
        except Todo.DoesNotExist:
            return JsonResponse({'error': 'Todo bulunamadı'}, status=404)

        if request.method == 'DELETE':
            todo.delete()
            return JsonResponse({'message': 'Todo silindi'})
    return JsonResponse({'error': 'Giriş yapılmadı'}, status=401)

@csrf_exempt
def todo_create(request):
    user = get_user_from_token(request)
    if user is not None:
        if request.method == 'POST':
            data = JSONParser().parse(request)
            data['user'] = user.id
            serializer = TodoSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)
    return JsonResponse({'error': 'Giriş yapılmadı'}, status=401)